# v0.1 release checklist

- [x] Draft README, repository folders and ignore rules.
- [x] Include supplied dashboard screenshot; visually inspect for personal information.
- [x] Inspect supplied files and recover original Python visual source.
- [x] Receive complete replacement PBIX and verify archive integrity.
- [x] Review both user-supplied query texts and save portable release copies.
- [x] User reports applying source parameter, successful refresh and date/board slicer checks in release copy.
- [x] Check supplied release copy archive integrity and Python source consistency.
- [ ] Review embedded model, other connections and actual relationships.
- [x] Verify official dataset/resource links and their OGL metadata; record attribution.
- [ ] Complete licence-conditions and embedded-data review; verify imported snapshot.
- [x] Owner confirms only public data and the two reviewed queries, with no private connections; portable path tested by owner.
- [ ] Independent binary-model inspection (not performed; documented limitation).
- [x] Inspect recovered script for credentials, personal paths and confidential data.
- [x] Record direct Python imports and visual field names from actual source.
- [ ] Runtime-test dependencies and verify setup in Power BI.
- [ ] Confirm known limitations accurately match implementation.
- [x] Owner approves public nkosimate/nhs-scotland-ae-performance-dashboard; no code licence selected.
- [x] Release bundle presented; owner explicitly approves publication.
- [ ] Create repository and push only approved files; tag v0.1 and publish release.

PBIX files are ignored until reviewed. After approval, add a narrow exception for the reviewed report. Check file size against current GitHub limits before choosing normal Git or Git LFS. Do not force-add unreviewed data or report files.
