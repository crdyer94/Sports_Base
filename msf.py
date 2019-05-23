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
        firstname = obj["firstName"]
        lastname = obj["lastName"]
        fullname = firstname + " " + lastname
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
