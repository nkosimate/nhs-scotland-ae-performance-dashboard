"""Reconstructed NHS Scotland A&E Power BI Python visual, not recovered verbatim.
Power BI supplies the filtered pandas DataFrame `dataset`.
Add Date and both additive count fields to the visual. Do not summarize Date.
Include row IDs if Power BI would otherwise collapse distinct source rows.
Never combine detail counts with overlapping national/board/department totals.
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

DATE_COLUMN = 'Date'
ATTENDANCES_COLUMN = 'Attendances'  # ASSUMED: map to actual model column
WITHIN_COLUMN = 'Within4Hours'  # ASSUMED: map to actual model column
WINDOW = 12
ANOMALY_SD = 2.0  # Reconstructed rule; earlier threshold unavailable
BENCHMARK = 95.0


def prepare_monthly(data):
    columns = [DATE_COLUMN, ATTENDANCES_COLUMN, WITHIN_COLUMN]
    missing = [c for c in columns if c not in data.columns]
    if missing:
        raise ValueError('Missing Power BI visual fields: ' + ', '.join(missing))
    frame = data[columns].copy()
    frame[DATE_COLUMN] = pd.to_datetime(frame[DATE_COLUMN], errors='coerce')
    if frame[DATE_COLUMN].isna().any():
        raise ValueError('Missing or invalid Date values.')
    for column in columns[1:]:
        original = frame[column]
        frame[column] = pd.to_numeric(original, errors='coerce')
        if (original.notna() & frame[column].isna()).any():
            raise ValueError(f'{column} contains nonnumeric values.')
    counts = frame[columns[1:]]
    if (counts.lt(0).any().any()
            or counts.isin([float('inf'), -float('inf')]).any().any()
            or (frame[WITHIN_COLUMN] > frame[ATTENDANCES_COLUMN]).any()):
        raise ValueError('Counts must be finite and satisfy 0 <= within <= attendances.')
    frame['Month'] = frame[DATE_COLUMN].dt.to_period('M').dt.to_timestamp()
    monthly = frame.groupby('Month')[columns[1:]].sum(min_count=1).sort_index()
    # Never use a partial total when any contributing count is missing.
    incomplete = frame[columns[1:]].isna().any(axis=1).groupby(frame['Month']).any()
    monthly.loc[incomplete, columns[1:]] = float('nan')
    if monthly.empty:
        return monthly
    monthly = monthly.reindex(pd.date_range(monthly.index.min(), monthly.index.max(), freq='MS'))
    monthly.index.name = 'Month'
    monthly['Performance'] = 100 * monthly[WITHIN_COLUMN].div(
        monthly[ATTENDANCES_COLUMN].where(monthly[ATTENDANCES_COLUMN] > 0))
    # Reindexing ensures 12 observations means 12 calendar months, without filling gaps.
    monthly['RollingMean'] = monthly['Performance'].rolling(WINDOW, min_periods=WINDOW).mean()
    history = monthly['Performance'].shift(1).rolling(WINDOW, min_periods=WINDOW)
    monthly['BaselineMean'] = history.mean()
    monthly['BaselineSD'] = history.std(ddof=1)
    monthly['Anomaly'] = (
        monthly['Performance'].sub(monthly['BaselineMean']).abs()
        > ANOMALY_SD * monthly['BaselineSD']
    ) & monthly['Performance'].notna() & monthly['BaselineSD'].notna()
    return monthly


def plot_dashboard(data):
    monthly = prepare_monthly(data)
    fig, ax = plt.subplots(figsize=(12, 5.5))
    valid = monthly.get('Performance', pd.Series(dtype=float)).dropna()
    if valid.empty:
        ax.text(0.5, 0.5, 'No valid attendance data in the selected period',
                ha='center', va='center', transform=ax.transAxes)
        ax.set_axis_off()
        return fig
    ax.plot(monthly.index, monthly['Performance'], color='#0072CE', linewidth=2,
            label='Monthly performance')
    ax.plot(monthly.index, monthly['RollingMean'], color='#E69F00', linewidth=2,
            label='12-month rolling average')
    unusual = monthly.loc[monthly['Anomaly']]
    ax.scatter(unusual.index, unusual['Performance'], color='#D62728', s=45,
               zorder=5, label='Unusual month (±2 SD)')
    ax.axhline(BENCHMARK, color='#64748B', linestyle='--', label='95% benchmark')
    date, value = valid.index[-1], valid.iloc[-1]
    ax.annotate(f'{date:%b %Y}: {value:.1f}%', xy=(date, value), xytext=(-10, 18),
                textcoords='offset points', ha='right', fontsize=9,
                arrowprops={'arrowstyle': '-', 'color': '#334155'},
                bbox={'boxstyle': 'round,pad=0.3', 'fc': 'white', 'ec': '#CBD5E1'})
    ax.set_title('A&E Performance: Rolling Trend and Unusual Months', loc='left', pad=14)
    ax.set_ylabel('Within 4 hours (%)')
    ax.set_ylim(0, 105)
    locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    ax.grid(axis='y', alpha=0.2)
    for side in ['top', 'right']:
        ax.spines[side].set_visible(False)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.13), ncol=2, frameon=False)
    fig.text(0.02, 0.015,
             'Mean: 12 complete months. Anomalies: 12 preceding complete months. '
             'Only Power BI-supplied history is available.', fontsize=8, color='#64748B')
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    return fig


if __name__ == '__main__':
    if 'dataset' not in globals():
        raise RuntimeError('Run in a Power BI Python visual supplying dataset.')
    plot_dashboard(dataset)
    plt.show()
