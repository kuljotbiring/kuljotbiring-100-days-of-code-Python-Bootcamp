from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

YOUR_UNIQUE_CLIENT_ID = "enter client ID"
YOUR_UNIQUE_CLIENT_SECRET = "enter client secret"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_UNIQUE_CLIENT_ID,
                                     client_secret=YOUR_UNIQUE_CLIENT_SECRET,
                                                                      show_dialog=True,
                                                                                  cache_path="token.txt"))
user_id = sp.current_user()["id"]

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)

# make the soup from parsing the website
soup = BeautifulSoup(response.text, "html.parser")

top_100_songs = soup.find_all(name="h3", class_="a-no-trucate")

song_titles = [song.getText().strip() for song in top_100_songs]

print(song_titles)

