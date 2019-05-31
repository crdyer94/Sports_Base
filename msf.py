#DEAL WITH PRETTY PRINT <-----------------
import os
import requests
from requests.auth import HTTPBasicAuth

MYSPORTSFEED_TOKEN = os.environ.get('MYSPORTSFEED_TOKEN')
MYSPORTSFEED_PASS = os.environ.get('MYSPORTSFEED_PASS')

SPORTSFEED_URL = "https://api.mysportsfeeds.com/v2.1/pull/nfl/"


def get_player_nflarrestlink(athlete_id):
    """Gets the player's name for other APIs"""
    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"players.json?player={athlete_id}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()

    response_players_dictionary = response.get("players")[0]
    player_dictionary = response_players_dictionary.get("player")


    nflarrestlinkname = player_dictionary.get("firstName") + "%20" + player_dictionary.get("lastName")

    return nflarrestlinkname

def get_player_name(athlete_id):
    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"players.json?player={athlete_id}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()

    response_players_dictionary = response.get("players")[0]
    player_dictionary = response_players_dictionary.get("player")


    full_name = player_dictionary.get("firstName") + player_dictionary.get("lastName")

    return full_name


def get_search_results(playername):
    """Gets the search from results from the API based on the entered player last name"""

    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"players.json?player={playername}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()

    response_display = []

    for obj in response["players"]:

        obj = obj["player"]

        fullname = obj.get("firstName") + " " + obj.get("lastName")
        athlete_id = obj["id"]

        athlete_route = {athlete_id:fullname}

        response_display.append(athlete_route)

    return response_display



# get the athlete_id, the first name, the last name from the API
# create dictionary as athlete_id: fullname
# add to list of results
# return list of dictionaries to server
# on server display fullname on screen
# when user clicks fullname, we route to a profile page for that specific athlete_id



def get_athlete_info(athlete_id):
    """Gets a player's info from API to display on that player's profile page"""

    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"players.json?player={athlete_id}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()

    response_players_dict = response.get("players")[0]
    player_dict = response_players_dict.get("player")

    response_team_dict = response.get("references")
    team_dict = response_team_dict.get("teamReferences")[0]
    arena = team_dict.get("homeVenue")

    player_profile = {
    "fullname": player_dict.get("firstName") + " " +
                player_dict.get("lastName"), 
    "position": player_dict.get("primaryPosition"),
    "h/weight": player_dict.get("height") + ", "+ 
                str(player_dict.get("weight")) + " lbs",
    "bday": player_dict.get("birthDate") + ", " + player_dict.get("birthCity"),
    "age": player_dict.get("age"),
    "highschool": player_dict.get("highSchool"),
    "college": player_dict.get("college"),
    "rosterpic": player_dict.get("officialImageSrc"),
    "current_team": team_dict.get("city") + " " + team_dict.get("name"),
    "team_abbr": team_dict.get("abbreviation"),
    "jersey_num": player_dict.get("jerseyNumber"), 
    "arena": arena.get("name")

    # "rosterstatus": player_dict.get("currentRosterStatus"),
    
    }

    return player_profile

def get_stats(athlete_id):
    """Gets the player's stats from API"""
    results = []
    career_data = {}
    available_seasons =  ["2019-playoff", "2018-2019-regular",
                            "2018-playoff", "2017-2018-regular"]
    available_seasons_count = 0

    for season in available_seasons:

        Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]
        response = requests.get(SPORTSFEED_URL + f"{season}/player_stats_totals.json?player={athlete_id}",
             auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
        response=response.json()

        response_stats_info = response.get("playerStatsTotals")[0] #keywords of dictionaries within the API's playerStatsTotals
        player_stats = response_stats_info.get("stats") #keywords of dictionaries within the API's stats

        if player_stats.get("gamesPlayed") != 0: #adds season stats in seasons the athlete played
        #WORKING ON PARSING HERE AS OF MAY 29
            career_data = {
            "season": season,
            "gamesPlayed": player_stats.get("gamesPlayed"),
            "passing": player_stats.get("Passing")
            }
            results.append(career_data)

    return player_stats




