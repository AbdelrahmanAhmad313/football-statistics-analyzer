from database import cursor


def getLeagueTableOptimized(league_id, season):
    cursor.execute("""
 SELECT
    t.team_long_name,
    SUM(points) AS total_points,
    SUM(goals_scored) AS goals_scored,
    SUM(goals_conceded) AS goals_conceded,
    SUM(goals_scored) - SUM(goals_conceded) AS goal_diff
FROM (
    SELECT
        home_team_api_id AS team_id,
        home_team_goal AS goals_scored,
        away_team_goal AS goals_conceded,
        CASE
            WHEN home_team_goal > away_team_goal THEN 3
            WHEN home_team_goal = away_team_goal THEN 1
            ELSE 0
        END AS points
    FROM Match
                   WHERE season =?
                   AND league_id=?

    UNION ALL

    SELECT
        away_team_api_id AS team_id,
        away_team_goal AS goals_scored,
        home_team_goal AS goals_conceded,
        CASE
            WHEN away_team_goal > home_team_goal THEN 3
            WHEN away_team_goal = home_team_goal THEN 1
            ELSE 0
        END AS points
    FROM Match
                   WHERE season =?
                   AND league_id=?
) AS league_table
                   JOIN Team AS t
                   ON team_id = t.team_api_id
GROUP BY team_id,
                   t.team_long_name
ORDER BY total_points DESC,
                   goal_diff DESC;
""",(season,league_id,season,league_id))
    result=cursor.fetchall()
    return result

def getLeagueId(league_name):
    cursor.execute("""
SELECT country_id
                   FROM League 
                   WHERE name LIKE ?

""",(f"%{league_name}%",))
    id = cursor.fetchone()
    return id[0]

def getLeagueTeams(league_id,season):
    cursor.execute("""
SELECT DISTINCT home_team_api_id
                   FROM Match
                   WHERE league_id = ? AND season = ?
""", (league_id, season))
    teams = cursor.fetchall()
    return teams
 