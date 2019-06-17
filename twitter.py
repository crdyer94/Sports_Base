import os
import tweepy
import requests
from mysportsfeed import my_sports_feed_players_api


TWITTER_CONSUMER = os.environ.get('TWITTER_CONSUMER')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS = os.environ.get('TWITTER_ACCESS')
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')


auth = tweepy.auth.OAuthHandler(TWITTER_CONSUMER, TWITTER_CONSUMER_SECRET)
auth.secure=True
auth.set_access_token(TWITTER_ACCESS, TWITTER_ACCESS_SECRET)

api = tweepy.API(auth)


def get_player_name(athlete_id):
    """ This calls the my sportsfeed api and returns the full name
     of the player to be used for searching"""
    api_response = my_sports_feed_players_api(athlete_id)
    api_player_dictionary = api_response.get("players")[0]

    player_dictionary = api_player_dictionary.get("player")

    full_name = player_dictionary.get("firstName") + " " + player_dictionary.get("lastName")

    return full_name


def get_player_tweets(athlete_id):
    """Gets the player's tweets from Twitter"""

    player_screen_name = get_player_screen_name(athlete_id)
    player_tweets =[]

    player_tweets_objects = api.user_timeline(screen_name=player_screen_name,
                                        trim_user="true",
                                        include_rts="false",
                                        exclude_replies="true",
                                        count=9)
    for tweet_object in player_tweets_objects:

        player_tweet_object = tweet_object._json
        player_tweet = player_tweet_object["text"]

        player_tweets.append(player_tweet)


    return player_tweets


def get_player_screen_name(athlete_id):
    """Gets the athlete's twitter from the Twitter API"""
    
    player_name = get_player_name(athlete_id)

    player_twitter_user_object = api.search_users(q=player_name, count=1)[0]

    player_twitter_user_information = player_twitter_user_object._json

    player_twitter_screen_name = player_twitter_user_information.get("screen_name")


    return player_twitter_screen_name

