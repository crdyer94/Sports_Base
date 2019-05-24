#DEAL WITH PRETTY PRINT <-----------------
import os
import requests
from flask import request
from requests.auth import HTTPBasicAuth

MYSPORTSFEED_TOKEN = os.environ.get('MYSPORTSFEED_TOKEN')
MYSPORTSFEED_PASS = os.environ.get('MYSPORTSFEED_PASS')

SPORTSFEED_URL = "https://api.mysportsfeeds.com/v2.1/pull/nfl/players.json"



def get_search_results(playername):
    """Gets the search from results from the API based on the entered player last name"""

    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"?player={playername}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()
    response_display = []
    for obj in response["players"]:
        obj = obj["player"]
        fullname = obj.get("firstName") + " " + obj.get("lastName")
        athlete_id = obj["id"]
        athlete_route = {athlete_id:fullname}


        response_display.append(athlete_route)


    # print(MYSPORTSFEED_PASS)
    # print (response.json())

    return response_display



# get the athlete_id, the first name, the last name from the API
# create dictionary as athlete_id: fullname
# add to list of results
# return list of dictionaries to server
# on server display fullname on screen
# when user clicks fullname, we route to a profile page for that specific athlete_id



def get_athlete_info(athlete_id):
    """Gets a player's API info to display on that player's profile page"""

    Authorization: Basic [MYSPORTSFEED_TOKEN + ":" + MYSPORTSFEED_PASS]

    response = requests.get(SPORTSFEED_URL + f"?player={athlete_id}",
         auth=HTTPBasicAuth(MYSPORTSFEED_TOKEN, MYSPORTSFEED_PASS))
    response=response.json()

    response_players_dict = response.get("players")[0]
    player_dict = response_players_dict.get("player")
    player_profile = {
    "fullname": player_dict.get("firstName") + " " +
                player_dict.get("lastName"), 
    "position": player_dict.get("primaryPosition"),
    "h/weight": player_dict.get("height") + ", "+ 
                str(player_dict.get("weight")) + "lbs",
    "bday": player_dict.get("birthDate") + ", " + player_dict.get("birthCity"),
    "age": player_dict.get("age"),
    "highschool": player_dict.get("highSchool"),
    "college": player_dict.get("college"),
    "rosterpic": player_dict.get("officialImageSrc")

    }



    return player_profile

 





# Team Stuff
#  player_dict{'jerseyNumber': 12, 'currentTeam': {'id': 50, 'abbreviation': 'NE'}, 
#  player_dict{'teamAsOfDate': {'id': 50, 'abbreviation': 'NE'}


# Player stuff to loop specifically
# # 'currentRosterStatus': 'ROSTER', 'currentInjury': None,































