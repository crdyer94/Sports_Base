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
    try:
        response = requests.get(f'http://nflarrest.com/api/v1/player/arrests/{player_name}', headers={'content-type': 'application/json',  'Accept': 'application/json, */*'}, cookies={'PHPSESSID':'00815b12f2388fca7f77c0a941372da1'})
    except RuntimeError:
        response = "THIS DIDNT WORK"
    print(response.request)
 
    return response
