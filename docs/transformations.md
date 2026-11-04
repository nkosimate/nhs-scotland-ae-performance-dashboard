# Transformation notes

The user has supplied the full AE_Activity Advanced Editor query. Its date conversion, explicit types and AttendanceCategory = "All" filter are confirmed in that supplied text. A parameterised release copy is saved in `powerquery/AE_Activity.pq`; it has not been executed here. The full Health_Boards Advanced Editor query has also been supplied and preserved in `powerquery/Health_Boards.pq`.

## AE_Activity

1. Import the monthly activity CSV and promote headers if necessary.
2. Interpret numeric Month (YYYYMM) as the first of that month:

```powerquery
#date(Number.IntegerDivide([Month], 100), Number.Mod([Month], 100), 1)
```

3. Filter AttendanceCategory to All to avoid overlapping attendance categories.
4. Assign date, text and numeric types.
5. Preserve quality flags and missing values; do not automatically replace nulls with zero.

## Health_Boards

Reference AE_Activity, keep HBT, remove duplicate codes and map codes to readable board names. Relate Health_Boards[HBT] (one) to AE_Activity[HBT] (many).

The supplied mapping covers 14 explicit codes and labels other codes "Unknown". The mapping is preserved as supplied, rather than independently validated. Historical codes, Unknown rows and the model relationship still need inspection.

## Needed to complete reproducibility

Both query texts are now available. Confirm they match the release PBIX, and inspect all other queries and connections. Replace any machine-specific file path with a configurable source path in the release copy, preserve the working original, and test refresh against the intended snapshot. Verify category filtering, missing values, board mapping and relationships in Power BI.
