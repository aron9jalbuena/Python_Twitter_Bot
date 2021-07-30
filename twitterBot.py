import tweepy
import time
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

hashtag = '#PokemonUNITE'

tweets = tweepy.Cursor(api.search, hashtag).items()

def searched():
	#Get all the tweets resulting in the hashtag and the number of tweets. 
	for tweet in tweets:
		#Retweets tweets that have #PokemonUNITE and atleast 100 likes
		if tweet.favorite_count > 100:
			try:
				tweet.retweet()
				print("Retweet Done!")
				time.sleep(1)
			except tweepy.TweepError as e:
				print(e.reason)
				time.sleep(1)
		else:
			print("Not Enough Likes")
   
while True:
        searched()
        time.sleep(600)
