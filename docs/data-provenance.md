# Data provenance

Publisher: Public Health Scotland (PHS).

- [Monthly A&E Activity and Waiting Times](https://www.opendata.nhs.scot/en/dataset/monthly-accident-and-emergency-activity-and-waiting-times)
- [Monthly Accident and Emergency Activity resource](https://www.opendata.nhs.scot/dataset/997acaa5-afe0-49d9-b333-dcf84584603d/resource/37ba17b1-c323-492c-87d5-e986aae9ab59)
- Licence listed by the official dataset and resource: UK Open Government Licence (OGL).
- [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- Metadata checked: 4 November 2026.

Attribution supplied for this project:

> Contains public sector information from Public Health Scotland, licensed under the Open Government Licence v3.0.

The official metadata confirms OGL; the licence text itself could not be retrieved by the browsing tool, so its full conditions have not been independently reviewed here. The project's code licence is a separate decision.

## Snapshot and refresh

The user identifies `monthly_ae_activity_202608.csv` as the imported snapshot. The original CSV and import query have not been inspected, so the snapshot's contents, hash and import date are unverified. The resource currently links to `monthly_ae_activity_202609.csv`, updated 3 November 2026. Do not silently substitute the latest file when reproducing the screenshot.

The official field dictionary includes Month, HBT, DepartmentType, AttendanceCategory and the attendance count columns referenced by the recovered Python visual.

PHS warns that `All` overlaps the constituent attendance categories. Filter to `All`, or use the constituents without `All`, to avoid double counting. This is a documented source requirement; its implementation in the report remains to be checked.

## Publication boundary

No CSV is bundled. The PBIX contains an embedded model; linking to the source does not remove that embedded data. Its tables, transformations, connections and any private paths still require inspection before publication. The reconstructed query description is in [transformation notes](transformations.md).
