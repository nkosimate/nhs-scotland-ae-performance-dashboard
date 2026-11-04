// User-supplied Health_Boards query; mapping preserved, not historically validated.
let
  Source = AE_Activity,
  #"Removed other columns" = Table.SelectColumns(Source, {"HBT"}),
  #"Removed duplicates" = Table.Distinct(#"Removed other columns", {"HBT"}),
  #"Added custom" = Table.AddColumn(#"Removed duplicates", "Health Board", each if [HBT] = "S08000015" then "NHS Ayrshire and Arran"
else if [HBT] = "S08000016" then "NHS Borders"
else if [HBT] = "S08000017" then "NHS Dumfries and Galloway"
else if [HBT] = "S08000019" then "NHS Forth Valley"
else if [HBT] = "S08000020" then "NHS Grampian"
else if [HBT] = "S08000022" then "NHS Highland"
else if [HBT] = "S08000024" then "NHS Lothian"
else if [HBT] = "S08000025" then "NHS Orkney"
else if [HBT] = "S08000026" then "NHS Shetland"
else if [HBT] = "S08000028" then "NHS Western Isles"
else if [HBT] = "S08000029" then "NHS Fife"
else if [HBT] = "S08000030" then "NHS Tayside"
else if [HBT] = "S08000031" then "NHS Greater Glasgow and Clyde"
else if [HBT] = "S08000032" then "NHS Lanarkshire"
else "Unknown")
in
  #"Added custom"
