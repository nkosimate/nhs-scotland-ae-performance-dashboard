# NHS Scotland A&E dashboard source

## Provenance
The accessible Build Python Dashboard conversation contains the final date-slicer fixes, but not the earlier Python source, base count-column names, original anomaly rule, or original display expression. The Python script and missing measure definitions are explicitly reconstructed; this is not a verbatim export of all original code. No NHS results or data are included. DAX has not been executed against the original Power BI model.

## Files and setup
- `ae_performance_anomaly_detection.py`: paste into a Power BI Python visual. Power BI supplies `dataset`; add Date and additive attendance/within-four-hours count fields. Map the two assumed names (`Attendances`, `Within4Hours`) in the constants to actual fields. Install pandas and matplotlib in the Python environment selected in Power BI.
- `powerbi_dax_measures.dax`: create the nine measures separately, in file order. Replace the same two assumed raw count-column references. `AE_Activity[Date]` is confirmed in the conversation.

Use raw additive counts, not percentages, and exclude overlapping aggregate rows. The Python calculation sums counts by month before dividing, rather than averaging board percentages. Missing/zero denominators stay unavailable. A month with any missing supplied count is unavailable; absent source rows cannot be detected without an expected coverage table.

## Dates and YoY
The recovered model uses a slicer directly on `AE_Activity[Date]`. Use the Date field itself, not its automatic hierarchy. Dates must consistently identify month-start or month-end. Latest KPIs use the latest date in the selected period and retain health-board/department filters. The previous-year measure targets that same month one year earlier, removing only the fact Date filter. YoY reuses that measure and returns numeric percentage points. Missing comparisons return blank. Month-end handling was added for leap years.

If your actual report filters through a related Calendar table, these definitions need adapting: take the selected reporting month from that table and clear its filters when retrieving the prior year. Clearing only the fact Date will not override a related Calendar slicer. A separate Calendar version is deliberately not mixed into this fact-date implementation.

Latest month is contextual: a board without the most recent month may select an earlier available month. A common-month board ranking remains a separate unresolved enhancement in the conversation.

## Rolling analysis
The trailing mean requires 12 complete calendar months including the current month. The reconstructed anomaly rule flags performance outside the preceding 12 complete months' mean ± two sample standard deviations. It excludes the current point from the baseline and requires at least 13 supplied months before flagging. These are exploratory flags, not statistical significance claims or a recovered original method.

Power BI filters `dataset` before Python runs. Python cannot recover months removed by the Date slicer. The beginning of a short selected range therefore has no rolling mean or anomaly baseline. The earlier conversation proposed a separate history-supplying model, but did not implement it in the retrieved turns; this package does not claim to resolve that model-level task. Last-point annotation refers to the latest nonmissing performance observation supplied.

## Validation
Python syntax was checked successfully. Runtime tests were not run because pandas and matplotlib are not installed in the available Python environment. No original `.pbix` or dataset was available, so model-specific DAX, actual column mappings, historical board comparability, and report filter interactions still require verification in Power BI. Test a single-year date selection, a board/department filter, missing prior-year data, and a leap-year month-end comparison.

## Optional Power Query
No `.pq` files are supplied because neither the original date-source fields nor an authoritative Health_Boards lookup was present in the retrieved history. Inventing codes or historical board mappings would undermine reproducibility.

## Reference
DAX selection semantics: https://learn.microsoft.com/en-us/dax/allselected-function-dax
