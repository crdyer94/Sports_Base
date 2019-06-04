#DEAL WITH PRETTY PRINT <-----------------
import os
import requests
from requests.auth import HTTPBasicAuth
from msf import my_sports_feed_players_api


def get_player_nflarrestlink(athlete_id):
    """Gets the player's name for other APIs
        This returns the athlete's name for the nfl arrest api link"""
    api_response = my_sports_feed_players_api(athlete_id)
    api_player_dictionary = api_response.get("players")[0]

    player_dictionary = api_player_dictionary.get("player")

    nflarrestlinkname = player_dictionary.get("firstName") + "%20" + player_dictionary.get("lastName")

    return nflarrestlinkname

def get_player_name(athlete_id):
    """ This returns the full name of the player to be used for the twitter api"""
    api_response = my_sports_feed_players_api(athlete_id)
    api_player_dictionary = api_response.get("players")[0]

    player_dictionary = api_player_dictionary.get("player")

    full_name = player_dictionary.get("firstName") + " " + player_dictionary.get("lastName")

    return full_name