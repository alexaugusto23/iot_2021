import tweepy
import autenticacao as aut
from datetime import datetime

# Autenticação Tweepy

auth = tweepy.OAuthHandler(aut.API_key, aut.API_key_secret)
auth.set_access_token(aut.access_token, aut.access_token_secret)

api = tweepy.API(auth)
date_time = datetime.now()

#Envia o tweet
tweet = f'Primeiro Tweet usando python!!! novo post {date_time.strftime("%d/%m/%Y %H:%M:%S")}'

try:
    api.update_status(tweet)
    print(f'Tweet Success {date_time.strftime("%d/%m/%Y %H:%M:%S")}')
except tweepy.TweepError as e:
    print(e.reason)