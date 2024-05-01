import os
import time
import pyautogui
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
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

clear_cache_script = """
tell application "Safari" to activate
delay 1 -- Wait for Safari to activate
tell application "System Events"
    tell process "Safari"
        click menu item "Empty Caches" of menu "Develop" of menu bar 1
    end tell
end tell
"""

def find_deviceID(type):
    devices = sp.devices()
    # print(devices)
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

def start_playback(playList=False):
    print("Starting Spotify playback...\n")

    joey = '3gJDgenxLephg09x86IxPs?si=6aad562132664b17'
    unofficialboyy = '2T4rkceZUut5d5boEM1iEP?si=583cdebc2bae430e'
    blackskirts = '4bjNOhOMvqFPflwHIaS7Fw?si=1dddecefbf404f43'
    onlyInMyMind = '4PrGyX4YgCT6V3YqY7XEUw?si=d42ef78b9cc8479a'

    # if playList option is on
    if playList:
        song_lst = [joey, unofficialboyy, blackskirts]

        for song in song_lst:
            track_uri = "spotify:track:" + song
            try:
                sp.start_playback(uris=[track_uri], device_id = find_deviceID('Computer'))
                time.sleep(30)
                sp.pause_playback()
            except spotipy.exceptions.SpotifyException as e:
                print(f"Error: {e}")
        return
    
    # song = blackskirts
    track_uri = "spotify:track:" + blackskirts

    # without playList option
    # Start playback
    try:
        sp.start_playback(uris=[track_uri], device_id = find_deviceID('Computer'))
        time.sleep(30)
        sp.pause_playback()
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error: {e}")

def spotify_action(playList=False):
    # Open Safari www.open.spotify.com
    os.system("open -a Safari http://open.spotify.com")

    # Execute the AppleScript to clear broswer cache
    # os.system(f"osascript -e '{clear_cache_script}'")
    # time.sleep(3)

    # open spotify app
    # os.system("open -a Spotify")
    print(sp.devices())
    time.sleep(30)
    # for loop number
    n = 10
    # playList = True
    # if playList:
    #     n = 10

    # play the same song 10 times
    for _ in range(n):
        # os.system(f"osascript -e '{clear_cache_script}'")
        time.sleep(3)
        start_playback()
        print(f"########## ITERATION: {_} ##########")

    time.sleep(3)
    
    # quit broswer
    os.system("osascript -e 'tell application \"Safari\" to quit'")
    # pyautogui.hotkey('command', 'w')

# spotify_action()