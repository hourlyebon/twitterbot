import tweepy
import os
import random

# Credenziali dalle variabili d'ambiente
api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Scegli immagine casuale dalla cartella "images"
images = os.listdir("images")
selected = random.choice(images)
image_path = f"images/{selected}"

# Pubblica su Twitter
api.update_status_with_media(status="", filename=image_path)
print(f"Pubblicato: {selected}")
