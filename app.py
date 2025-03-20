import spotipy, os, pyaudio
import speech_recognition as sr
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load the .env variables
load_dotenv()

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="URL",
        scope="playlist-read-private playlist-modify-private user-library-modify"
    )
)

# Get Spotify user ID
user = spotify.me()["id"]

# Your playlist id
playlist_id = ""

def get_playlist_songs(playlist_id):
    songs = []
    results = spotify.playlist_tracks(playlist_id, limit=100)
    
    while results:
        for song in results["items"]:
            track = song["track"]
            if track:
                songs.append(
                    (
                        track["id"],
                        track["name"],
                        track["artists"][0]["name"],
                        track["album"]["name"]
                    )
                )
        results = spotify.next(results) if results["next"] else None
    return songs

def find_repeated_songs(songs):
    ids = set()
    repeated = []

    for track_id, name, artists, album in songs:
        if track_id in ids:
            repeated.append(track_id)
            # print(f"repeated song: {track_id}")
        else:
            ids.add(track_id)
    return repeated

def remove_repeated_songs_from_playlist(playlist_id, repeated):
    
    if repeated:

        # We create an independent copy of the 'repeated' list
        single_track = repeated[:]
        single_track = list(set(single_track))

        # We apply the format that spotify needs to work
        repeated = [f"spotify:track:{track_id}" for track_id in repeated]

        # This line, actually removes ALL ocurrences of the repeated songs
        # even the one we want to keep.
        spotify.playlist_remove_all_occurrences_of_items(playlist_id, repeated)

        # This one do the trick. Inserts the songs of 'single_track' list
        spotify.playlist_add_items(playlist_id, single_track)

        print(f"{len(repeated)} songs were removed.")
    else:
        print(f"There are not songs to eliminate.")

def voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        command = recognizer.listen(source)
    try:
        # You can change the language recognition if needed
        txt = recognizer.recognize_google(command, language="en")
        return txt.lower()
    except sr.UnknownValueError:
        return "Unrecognized"
    except sr.RequestError:
        return "API Error"

# Get all the songs of the playlist
playlist_songs = get_playlist_songs(playlist_id)

# Get all the repeated songs
repeated_songs = find_repeated_songs(playlist_songs)

command = voice_command()
if "remove" in command:

    # Remove the ocurrences of the songs
    # If song appears 4 times, remove 3 ocurrences
    remove_repeated_songs_from_playlist(playlist_id, repeated_songs)


