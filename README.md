# spotify-remove-repeated-songs
Remove the repeated song in a playlist in spotify with AI.

1.- Create an .env file to put yor credentials in this format:

SPOTIPY_CLIENT_ID="YOUR_CLIENT_ID" 
SPOTIPY_CLIENT_SECRET="YOUR_CLIENT_SECRET" 
SPOTIPY_REDIRECT_URI="URL"

2.- Load yor .env variables with load_dotenv(). 
3.- Authenticate and get Spotify user (just to ensure connection).

IMPORTANT: To get the ID of the playlist you want to modify, you can do this:
Go to your Spotify App
Right click on the Playlist -> Share -> Copy link -> https://open.spotify.com/playlist/#THIS_IS_YOUR_PLAYLIST_ID
