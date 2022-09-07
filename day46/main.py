from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)

# make the soup from parsing the website
soup = BeautifulSoup(response.text, "html.parser")

top_100_songs = soup.find_all(name="h3", class_="a-no-trucate")

song_titles = [song.getText().strip() for song in top_100_songs]

print(song_titles)

