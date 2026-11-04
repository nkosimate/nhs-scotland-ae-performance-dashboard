# Supplied file review

## Replacement PBIX

The replacement supplied from the sibling chat outputs folder is 618,857 bytes, with SHA-256 `9f8e4834f5909de88bb595c8d7bee83b70a7cd9eb073678004d5c5f0e1501345`. All 26 ZIP entries pass archive CRC checks. This establishes archive integrity, not successful opening or refresh in Power BI.

The embedded DataModel is present (596,528 uncompressed bytes). Its binary contents have not been decoded, so source provenance, embedded tables, queries, credentials and private paths cannot yet be cleared for publication. The PBIX is held outside the publication folder pending review. The earlier truncated copy is superseded.

## Python and examples

The original Python visual matches the previously recovered source exactly and passes AST syntax validation. Dependencies are not installed locally; no runtime or Power BI execution is claimed. No apparent credentials, personal filesystem paths or embedded source records were found in the script on manual inspection.

The separately supplied source package explicitly identifies its Python and several DAX measures as reconstructions. These are preserved as examples, not represented as original report code. No source datasets or PBIX files are included in the publication draft. Official dataset and resource URLs have been checked and list OGL. The imported snapshot, complete licence conditions and embedded model remain to be reviewed.

## AE_Activity query supplied in chat

The full query confirms a local CSV import, 27-column schema including `_id`, explicit types, month-start Date conversion and AttendanceCategory = "All" filtering. The personal source path is omitted from the publication files and replaced with a Text parameter. This query text has not been independently extracted from the binary model or runtime-tested. The embedded model still requires review. The filename does not verify the CSV snapshot date.

## Health_Boards query supplied in chat

The full reference query has been saved with its 14 explicit board-code mappings and Unknown fallback preserved. The text contains no personal paths or credentials. Historical validity and actual model relationship have not been verified. Supplying both query texts does not independently establish that the binary model contains only these queries or only public data.

## Release copy supplied after setup

The user supplied HS_AE_Dashboard_v0.1.pbix after reporting successful parameter setup, refresh and slicer checks. Size: 637718 bytes. SHA-256: `3d988d7c45873078098ea675c19db28e5687d40df6347b0b2ca28720ee3748bf`. ZIP integrity passes; the Python visual matches the release source. The copy is held outside publication files pending final embedded-model review. Parameter value, all model tables and connections have not been independently decoded. User-reported refresh and interaction checks are recorded as such, not independently executed.

## Updated portable-path release copy

SHA-256: `00e31723764b30f177ddeed4ece36bb5fd6c16a500792753d70b71b302fc409b`; size: 637785 bytes. Archive integrity passes and Python source matches. User reports changing SourceCsvPath to C:\Data\nhs_ae_activity.csv, placing the CSV there, then successfully applying, refreshing and saving. This is user-confirmed; the saved parameter and binary model have not been independently decoded. The PBIX remains outside the publication folder pending final review and publication approval.

## Owner content confirmation

The owner explicitly confirms that the release report contains only public information, with only the two reviewed queries and no other private data or connections. Based on that confirmation, the final report is staged as NHS_AE_Dashboard_v0.1.pbix. Binary model inspection remains a stated limitation; publication still requires separate approval.
