import os
import requests
from flask import request
from msf import get_player_nflarrestlink


NFLARREST_URL = 'http://nflarrest.com/api/v1/player/arrests'


def get_arrests(athlete_id):
    """Gets arrest information based on the athlete's full name"""

    player_name = get_player_nflarrestlink(athlete_id)
    # link_name = NFLARREST_URL + f'/{player_name}'
    # print(link_name)
    response = requests.get(
            f'http://nflarrest.com/api/v1/player/arrests/{player_name}', 
            headers={'user-agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'})


 
    return response.text
