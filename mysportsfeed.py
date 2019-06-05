#DEAL WITH PRETTY PRINT <-----------------
import os
import requests
from requests.auth import HTTPBasicAuth

MYSPORTSFEED_TOKEN = os.environ.get('MYSPORTSFEED_TOKEN')
MYSPORTSFEED_PASS = os.environ.get('MYSPORTSFEED_PASS')

SPORTSFEED_URL = "https://api.mysportsfeeds.com/v2.1/pull/nfl/"

def my_sports_feed_players_api(api_parameter):
    """Calls the players data from the mysportsfeed api"""
    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"players.json?player={api_parameter}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()

    return response

def get_search_results(playername):
    """Gets the search from results from the API based on the entered player last name
        My sports feed API requires a player's last name to search"""

    if " " in playername:
        playername_list = playername.split()
        api_playername = f"{playername_list[0]}-{playername_list[1]}"
    else:
        api_playername = playername

    response = my_sports_feed_players_api(api_playername)

    response_display = []

    for obj in response["players"]:

        obj = obj["player"]

        fullname = obj.get("firstName") + " " + obj.get("lastName")
        athlete_id = obj["id"]

        athlete_route = {athlete_id:fullname}

        response_display.append(athlete_route)

    return response_display

def get_athlete_info(athlete_id):
    """Gets a player's info from API to display on that player's profile page"""

    api_response = my_sports_feed_players_api(athlete_id)

    api_player_dictionary = api_response.get("players")[0]
    player_dictionary = api_player_dictionary.get("player")

    api_response_team_reference = api_response.get("references")
    team_dictionary = api_response_team_reference.get("teamReferences")[0]
    
    arena = team_dictionary.get("homeVenue")

    player_profile = {
    "fullname": player_dictionary.get("firstName") + " " +
                player_dictionary.get("lastName"), 
    "position": player_dictionary.get("primaryPosition"),
    "h/weight": player_dictionary.get("height") + ", "+ 
                str(player_dictionary.get("weight")) + " lbs",
    "bday": player_dictionary.get("birthDate") + ", " + player_dictionary.get("birthCity"),
    "age": player_dictionary.get("age"),
    "highschool": player_dictionary.get("highSchool"),
    "college": player_dictionary.get("college"),
    "rosterpic": player_dictionary.get("officialImageSrc"),
    "current_team": team_dictionary.get("city") + " " + team_dictionary.get("name"),
    "team_abbr": team_dictionary.get("abbreviation"),
    "jersey_num": player_dictionary.get("jerseyNumber"), 
    "arena": arena.get("name")

    # "rosterstatus": player_dict.get("currentRosterStatus"),
    
    }

    return player_profile

def get_stats(athlete_id):
    """Gets the player's stats from API"""
    career_stats = {
        "career_passing": [],
        "career_rushing": [],
        "career_receiving": [],
        "career_tackles": [],
        "career_interceptions": [],
        "career_fumbles": [],
        "career_kickoffReturns": [],
        "career_puntReturns": [],
        "career_twoPointAttempts": []
    }
    season_time = {}
    games_played = {}

    stat_types = ["passing", "rushing", "receiving", "tackles", 
                    "interceptions", "fumbles", "kickoffReturns", 
                    "puntReturns", "twoPointAttempts"]
    
    available_seasons =  ["2019-playoff", "2018-2019-regular",
                            "2018-playoff", "2017-2018-regular"]
    available_stat_categories = [("passing", "passAttempts"),
                                 ("rushing", "rushAttempts"),
                                 ("receiving", "targets"), 
                                 ("tackles", "tackleTotal"),
                                 ("interceptions", "interceptions"),
                                 ("fumbles", "fumbles"), 
                                 ("kickoffReturns", "krRet"),
                                 ("puntReturns", "prRet"), 
                                 ("twoPointAttempts", "twoPtAtt")]

    for available_season in available_seasons:

        Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]
        response = requests.get(SPORTSFEED_URL + f"{available_season}/player_stats_totals.json?player={athlete_id}",
             auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
        response=response.json() #this is a dictionary

        api_playerStatTotals = response.get("playerStatsTotals")[0]

        season_stats = api_playerStatTotals.get("stats")

        if season_stats["gamesPlayed"] != 0: #do not want to show seasons that the player did not participate in

            games_played = {"Games Played" : season_stats["gamesPlayed"]}
            season_time = {"Season": available_season}

            for category in available_stat_categories:

                if season_stats[category[0]][category[1]] != 0: #do not want to show stat categories that do not apply to the player
                    key = f'career_{category[0]}'
                    career_stats[key].append(season_time)
                    career_stats[key].append(games_played)
                    career_stats[key].append(season_stats[category[0]])
                        

    return career_stats





