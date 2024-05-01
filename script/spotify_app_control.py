import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
import shutil
from dotenv import load_dotenv

# load .env variables
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

scope = "user-modify-playback-state user-read-playback-state app-remote-control"

# intialize spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope=scope))

def find_deviceID(type):
    devices = sp.devices()
    device_id = None
    device_name = None

    for device in devices['devices']:
        if device['type']==type:
            device_id = device['id']
            device_name = device['name']
            break

    if not device_id:
        print(f"No {type}  found")
    else:
        print(f"{type} device found...")
        print(f"Device name: {device_name}")
        print(f"Active device ID: {device_id}\n")
        return device_id

def start_playback():
    print("Starting Spotify playback...\n")

    joey = '3gJDgenxLephg09x86IxPs'
    unofficialboyy = '2T4rkceZUut5d5boEM1iEP'
    blackskirts = '4bjNOhOMvqFPflwHIaS7Fw'
    onlyInMyMind = '4PrGyX4YgCT6V3YqY7XEUw'

    track_uri = "spotify:track:" + blackskirts

    # Start playback
    try:
        # print(sp.current_user_playing_track())
        sp.start_playback(uris=[track_uri], device_id = find_deviceID('Computer')) # device_id = 9ae55c5d2aec204af32030921d921a85a479ebf9
        time.sleep(30)
        sp.pause_playback()
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error: {e}")

def clear_directory(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # if os.path.isfile(item_path):
        #     os.remove(item_path)  # Remove the file
        if os.path.isdir(item_path):
            # Clear the directory's contents instead of removing the directory
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)
                if os.path.isfile(subitem_path):
                    os.remove(subitem_path)
                else:  # It's a directory
                    shutil.rmtree(subitem_path)

def spotify_action():
    # clear Spotify cache first
    spotify_cache_directory = '/Users/minocha/Library/Application Support/Spotify/PersistentCache/Storage'
    clear_directory(spotify_cache_directory)

    # time.sleep(3)

    # open spotify app
    os.system("open -a Spotify")
    # time.sleep(30)
    # print(sp.devices())

    # play the same song 10 times
    for _ in range(10):
        clear_directory(spotify_cache_directory)
        time.sleep(3)
        start_playback()
        print(f"########## ITERATION: {_} ##########")

    time.sleep(3)
    # quit spotify app
    os.system("osascript -e 'tell application \"Spotify\" to quit'")

# spotify_action()