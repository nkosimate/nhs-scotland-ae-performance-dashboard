# Power Query setup

`AE_Activity.pq` preserves the user-supplied Advanced Editor transformations, with the personal Windows source path replaced by `SourceCsvPath`. It has not been executed in Power BI here.

1. Obtain the intended CSV snapshot from the official resource documented in `docs/data-provenance.md`. The supplied query uses a resource-ID filename; its name alone does not establish the snapshot date.
2. In Power Query, choose Manage Parameters → New Parameter. Name it `SourceCsvPath`, choose Text and set its current value to the full local CSV path.
3. In a copy of your report, replace AE_Activity's Advanced Editor code with `AE_Activity.pq`.
4. Apply changes and verify refresh, row counts, date range and dashboard measures before replacing your working report.

The query expects 27 CSV columns, including `_id`, and preserves the original strict type conversions and `QuoteStyle.None`. A direct-download CSV may differ from a portal export. Confirm the schema first; a missing `_id`, changed column count or nonnumeric count marker may require an explicit adaptation. No automatic replacement of missing counts with zero has been added.

`Health_Boards.pq` preserves the actual query supplied by the user. Create or update Health_Boards after AE_Activity, then verify the one-to-many relationship from Health_Boards[HBT] to AE_Activity[HBT] in Model view. The query alone does not establish the relationship. Its 14-code mapping returns "Unknown" for every unlisted code; inspect those rows and validate historical codes before relying on long-term board comparisons. Before sharing a revised PBIX, remove personal parameter values from the publication copy and verify all its queries and connections.
