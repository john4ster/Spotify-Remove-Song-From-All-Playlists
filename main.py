import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys

CLIENT_ID = "insert_client_id"
CLIENT_SECRET = "insert_client_secret"
REDIRECT_URI = "https://removefromplaylists"

#Spotify api scopes to read and write to playlists
read_scope = "user-library-read"
write_scope = "playlist-modify-public"
#Command line arguments
song = sys.argv[1]
artist = sys.argv[2]

#Song found is false by default, will change to true if the song is found in any playlists
song_found = False

#Set up scopes
public_read = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri=REDIRECT_URI,
                                                        scope=read_scope))
public_modify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri=REDIRECT_URI,
                                                        scope=write_scope))

#Playlist results
public_results = public_read.current_user_playlists()
#Offset used to get the playlist_id rather than the full uri of each playlist, each uri is returned 
#as spotify:playlist:[playlist_id], so this offset will be used to just get the playlist_id
id_offset = 17
#Loop through each playlist
print("Attempting to remove song from all playlists...")
for playlist in public_results["items"]:
  #Get the id of each playlist
  current_playlist_id = playlist["uri"][id_offset:]
  #Get items in each playlist
  playlist_tracks = public_read.user_playlist_tracks(user=public_read.user, playlist_id=current_playlist_id)
  #Get name of each track in each playlist
  for track in playlist_tracks["items"]:
    #Get each track's name and first listed artist to compare against arguments
    track_name = track["track"]["name"]
    track_artist = track["track"]["artists"][0]["name"]
    #Get track's uri to remove it if it matches the arguments
    track_uri= track["track"]["uri"]
    #If the song was found, remove it from the playlist
    if song == track_name and artist == track_artist:
      public_modify.user_playlist_remove_all_occurrences_of_tracks(user=public_read.user, playlist_id=current_playlist_id, tracks=[track_uri])
      song_found = True
#Inform the user whether the song was found or not
if song_found:
  print("Song successfuly deleted from all playlists")
else:
  print("Song not found, please make sure you are entering the exact title.")
  print("Check the README for examples of common argument errors.")