# spotify-remove-repeated-songs
Remove the repeated song in a playlist in spotify with AI.

1.- Create an .env file to put yor credentials in this format:

SPOTIPY_CLIENT_ID="YOUR_CLIENT_ID" 
SPOTIPY_CLIENT_SECRET="YOUR_CLIENT_SECRET" 
SPOTIPY_REDIRECT_URI="URL"

2.- Load yor .env variables with load_dotenv(). 
3.- Authenticate and get Spotify user (just to ensure connection).

# IMPORTANT 1: 
To get the ID of the playlist you want to modify, you can do this:
Go to your Spotify App
Right click on the Playlist -> Share -> Copy link -> https://open.spotify.com/playlist/#THIS_IS_YOUR_PLAYLIST_ID

# IMPORTANT 2: 
This code uses playlist-read-private, playlist-modify-private and user-library-modify. This allows you to read and modify the user private playlists.
If your account is at risk, someone could modify or delete content of the playlists.
In a secure enviroment, you could use minimum permissions and ask for confirmation before any action.
