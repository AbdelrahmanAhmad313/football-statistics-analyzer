from database import cursor

def getMatches():
    cursor.execute("""
SELECT
    home.team_long_name,
    Match.home_team_goal,
    Match.away_team_goal,
    away.team_long_name
FROM Match
JOIN Team AS home
    ON Match.home_team_api_id = home.team_api_id
JOIN Team AS away
    ON Match.away_team_api_id = away.team_api_id
LIMIT 10;
""")
    match=cursor.fetchall()
    return match


def getWins(team_name, season=None, league_id= None):
    query="""SELECT COUNT(*)
               FROM Match
               JOIN Team AS home
                   ON Match.home_team_api_id = home.team_api_id
                JOIN Team AS away
                     ON Match.away_team_api_id = away.team_api_id 
                     WHERE (
               (home.team_long_name = ? AND Match.home_team_goal > Match.away_team_goal) 
               OR
               (away.team_long_name = ? AND Match.away_team_goal > Match.home_team_goal)
                 )
               
               """
    params =[team_name,team_name]

    if league_id is not None:
        query+=" AND league_id= ? "
        params.append(league_id)

    
    if season is not None:
        query+=" AND Match.season = ? "
        params.append(season)

    
    cursor.execute(query, params)
    result = cursor.fetchone()
    return result[0]

def getDraws(team_name,season=None,league_id=None):
    query="""
    SELECT COUNT(*)
    FROM Match
    JOIN Team AS home
               ON Match.home_team_api_id = home.team_api_id
               JOIN Team AS away
               ON Match.away_team_api_id = away.team_api_id
               WHERE 
               (home.team_long_name = ? OR away.team_long_name = ?)
               AND Match.home_team_goal = Match.away_team_goal 

        
"""
    params=[team_name,team_name]

    if season is not None:
        query+=" AND Match.season = ? "
        params.append(season)

    if league_id is not None:
        query+=" AND League_id = ? "    
        params.append(league_id)

    cursor.execute(query,params)
    result = cursor.fetchone()
    return result[0]

def getLosses(team_name,season=None,league_id=None):
    query= """
    SELECT COUNT(*)
    FROM Match
    JOIN Team AS home
                   ON Match.home_team_api_id = home.team_api_id
                JOIN Team AS away
                     ON Match.away_team_api_id = away.team_api_id
               WHERE 
               (
               (home.team_long_name = ? AND Match.home_team_goal < Match.away_team_goal)
               OR
               (away.team_long_name = ? AND Match.away_team_goal < Match.home_team_goal)
               )
            """
    params=[team_name,team_name]
    if season is not None:
        query+=" AND Match.season = ? "
        params.append(season)
    if league_id is not None:
        query+=" AND Match.league_id = ? "
        params.append(league_id)
    
    cursor.execute(query,params)
    result = cursor.fetchone()
    return result[0]

def getGoalsScored(team_name,season = None,league_id=None):

    query="""
 SELECT SUM(goals) as goals_scored
                  FROM (
SELECT home_team_goal AS goals,
        home_team_api_id AS team_id,
               season,
               league_id
                   FROM Match
                   UNION ALL
       SELECT away_team_goal AS goals,
        away_team_api_id AS team_id,
               season,
               league_id
                   FROM Match  
                   )          
                   JOIN Team AS t
                   ON team_id = t.team_api_id
                   WHERE team_long_name =?
"""
    params=[team_name]
    if season is not None:
        query+=" AND season =? "
        params.append(season)

    if league_id is not None:
        query+=" AND league_id =? "
        params.append(league_id)

    cursor.execute(query,params)
    result=cursor.fetchone()
    if result[0] is None:
        return 0

    return result[0]

def getGoalsConceded(team_name,season = None , league_id=None):
    query="""
    SELECT SUM(goals) AS goals_conceded
    FROM(
    SELECT
     away_team_goal AS goals,
     home_team_api_id AS team_id,
     League_id,
     season
     FROM Match
     UNION ALL
     SELECT
     home_team_goal AS goals,
     away_team_api_id AS team_id,
     League_id,
     season
     FROM Match 
         )
         JOIN Team AS t
                   ON team_id = t.team_api_id
                   WHERE team_long_name =?
"""
    params=[team_name]
    if season is not None:
        query+=" AND season =? "
        params.append(season)

    if league_id is not None:
        query+=" AND league_id =? "
        params.append(league_id)

    cursor.execute(query,params)
    result=cursor.fetchone()
    if result[0] is None:
        return 0

    return result[0]

def getGoalDifference(team_name,season=None,league_id=None):
    goals_scored = getGoalsScored(team_name,season,league_id)
    goals_conceded= getGoalsConceded(team_name,season,league_id)
    return goals_scored - goals_conceded

def getPoints(team_name, season=None, league_id=None):
    wins =getWins(team_name,season)*3
    draws= getDraws(team_name,season)
    return  wins + draws





def getTeamId(team_name):
    cursor.execute("""
            SELECT team_api_id
                   FROM Team
                   WHERE team_long_name = ?
""",(team_name,))
    result = cursor.fetchone()
    return result[0]


def getTeamName(team_id):

    cursor.execute(""" 
SELECT team_long_name 
                   FROM Team 
                   WHERE team_api_id = ?
""", (team_id,))
    name = cursor.fetchone()
    return name[0]


def getTeamStats(team_name, season=None, league_id=None):

    wins = getWins(team_name, season, league_id)
    draws = getDraws(team_name, season, league_id)
    losses = getLosses(team_name, season, league_id)

    goals_scored = getGoalsScored(team_name, season, league_id)
    goals_conceded = getGoalsConceded(team_name, season, league_id)

    goal_difference = getGoalDifference(team_name, season, league_id)
    points = getPoints(team_name, season, league_id)

    return {
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "goals_scored": goals_scored,
        "goals_conceded": goals_conceded,
        "goal_difference": goal_difference,
        "points": points
    }
