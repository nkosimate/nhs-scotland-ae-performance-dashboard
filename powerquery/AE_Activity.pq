// Release copy of user-supplied AE_Activity query.
// Create a Text parameter named SourceCsvPath with the full path to your CSV.
// Only the source path has been parameterised; transformation logic is preserved.
let
    Source = Csv.Document(File.Contents(SourceCsvPath), [Delimiter = ",", Columns = 27, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
    #"Promoted headers" = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),
    #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {
        {"_id", Int64.Type},
        {"Month", Int64.Type},
        {"Country", type text},
        {"HBT", type text},
        {"TreatmentLocation", type text},
        {"DepartmentType", type text},
        {"AttendanceCategory", type text},
        {"NumberOfAttendancesAll", Int64.Type},
        {"NumberWithin4HoursAll", Int64.Type},
        {"NumberOver4HoursAll", Int64.Type},
        {"PercentageWithin4HoursAll", type number},
        {"NumberOfAttendancesEpisode", Int64.Type},
        {"NumberOfAttendancesEpisodeQF", type text},
        {"NumberWithin4HoursEpisode", Int64.Type},
        {"NumberWithin4HoursEpisodeQF", type text},
        {"NumberOver4HoursEpisode", Int64.Type},
        {"NumberOver4HoursEpisodeQF", type text},
        {"PercentageWithin4HoursEpisode", type number},
        {"PercentageWithin4HoursEpisodeQF", type text},
        {"NumberOver8HoursEpisode", Int64.Type},
        {"NumberOver8HoursEpisodeQF", type text},
        {"PercentageOver8HoursEpisode", type number},
        {"PercentageOver8HoursEpisodeQF", type text},
        {"NumberOver12HoursEpisode", Int64.Type},
        {"NumberOver12HoursEpisodeQF", type text},
        {"PercentageOver12HoursEpisode", type number},
        {"PercentageOver12HoursEpisodeQF", type text}
    }, "en-US"),
    #"Added custom" = Table.AddColumn(#"Changed column type", "Date", each #date(
        Number.IntegerDivide([Month], 100),
        Number.Mod([Month], 100),
        1
    )),
    #"Changed column type 1" = Table.TransformColumnTypes(#"Added custom", {{"Date", type date}}),
    #"Filtered rows" = Table.SelectRows(#"Changed column type 1", each ([AttendanceCategory] = "All"))
in
    #"Filtered rows"
