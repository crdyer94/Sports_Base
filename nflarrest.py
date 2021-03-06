
import os
import requests
from flask import request
from mysportsfeed import my_sports_feed_players_api


NFLARREST_URL = 'http://nflarrest.com/api/v1/player/arrests'



def get_player_nflarrestlink(athlete_id):
    """Gets the player's name from the my sportsfeed api
        This returns the athlete's name for the nfl arrest api link"""
    api_response = my_sports_feed_players_api(athlete_id)
    api_player_dictionary = api_response.get("players")[0]

    player_dictionary = api_player_dictionary.get("player")

    nflarrestlinkname = player_dictionary.get("firstName") + "%20" + player_dictionary.get("lastName")

    return nflarrestlinkname


def get_arrests(athlete_id):
    """Gets arrest information based on the athlete's full name"""

    player_name = get_player_nflarrestlink(athlete_id)
    link_name = NFLARREST_URL + f'/{player_name}'
    
    try:
       
        response = requests.get(
                f'http://nflarrest.com/api/v1/player/arrests/{player_name}', 
                headers={'user-agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'})

        api_player_arrest_information = response.json()[0]
        player_arrest_information = { 
                                "Arrest Date" : api_player_arrest_information.get("Date"),
                                "Crime Category" : api_player_arrest_information.get("Crime_category") 
                                + ": " + api_player_arrest_information.get("Category"), 
                                "Description": api_player_arrest_information.get("Description"),
                                "Outcome": api_player_arrest_information.get("Outcome")
                                                }
        return player_arrest_information
    except Exception:
        player_arrest_information = handle_bad_arrest_response()
        return player_arrest_information


def handle_bad_arrest_response():
    """Handles responses for players that do not have any arrests"""
    
    arrest_error_response = { 
                                "Arrest Date" : "",
                                "Crime Category" : "",
                                "Description": "No arrests found for this player",
                                "Outcome": ""
                                                }
    return arrest_error_response