# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Date, NumberOfAttendancesAll, NumberWithin4HoursAll)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Power BI supplies the filtered data as 'dataset'
df = dataset.copy()

df["Date"] = pd.to_datetime(df["Date"])

# Aggregate attendances by month
monthly = (
    df.groupby("Date", as_index=False)
    .agg(
        attendances=("NumberOfAttendancesAll", "sum"),
        within4=("NumberWithin4HoursAll", "sum")
    )
    .sort_values("Date")
)

# Calculate weighted monthly performance
monthly = monthly[monthly["attendances"] > 0].copy()

monthly["performance"] = (
    monthly["within4"] / monthly["attendances"] * 100
)

# 12-month rolling average
monthly["rolling_avg"] = (
    monthly["performance"]
    .rolling(window=12, min_periods=6)
    .mean()
)

# Flag months unusually below the preceding 12-month trend
monthly["baseline"] = (
    monthly["performance"].shift(1)
    .rolling(window=12, min_periods=6)
    .mean()
)

monthly["baseline_std"] = (
    monthly["performance"].shift(1)
    .rolling(window=12, min_periods=6)
    .std()
)

monthly["anomaly"] = (
    monthly["performance"]
    < monthly["baseline"] - 2 * monthly["baseline_std"]
)

# Create visual
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly["Date"],
    monthly["performance"],
    label="Monthly performance",
    color="#3182CE",
    alpha=0.65
)

ax.plot(
    monthly["Date"],
    monthly["rolling_avg"],
    label="12-month rolling average",
    color="#E67E22",
    linewidth=2.5
)

anomalies = monthly[monthly["anomaly"]]

ax.scatter(
    anomalies["Date"],
    anomalies["performance"],
    color="#D62828",
    s=45,
    label="Unusually poor month",
    zorder=5
)

ax.axhline(
    95,
    color="gray",
    linestyle="--",
    linewidth=1,
    label="95% standard"
)

ax.set_title(
    "A&E Performance: Rolling Trend and Unusual Months",
    fontsize=13,
    fontweight="bold"
)

ax.set_ylabel("Within 4 hours (%)")
ax.set_xlabel("Month")
ax.grid(axis="y", alpha=0.2)
ax.legend(loc="best", fontsize=9)
ax.annotate(
    f'{monthly["performance"].iloc[-1]:.2f}%',
    xy=(
        monthly["Date"].iloc[-1],
        monthly["performance"].iloc[-1]
    ),
    xytext=(-35, 15),
    textcoords="offset points",
    fontsize=10,
    fontweight="bold",
    color="#3182CE"
)
plt.tight_layout()
plt.show()
