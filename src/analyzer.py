from stats import getTeamStats
from league_table import getLeagueId, getLeagueTableOptimized


print(getTeamStats("FC Barcelona"))

print(getTeamStats("FC Barcelona", season="2015/2016"))

print(getTeamStats("FC Barcelona", league_id=21518))

print(getTeamStats(
    "FC Barcelona",
    season="2015/2016",
    league_id=21518
))