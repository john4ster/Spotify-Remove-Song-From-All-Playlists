# Remove Song From All Spotify Playlists
Spotify has no option to remove a song from all your playlists. You have to manually go through each playlist and remove the song. This can be an annoying process, and can even lead to you forgetting to remove the song from some playlists. So I made this simple python script that you can use to remove a song from all your Spotify playlists at once.

# How to use
First, you need to replace the "Client ID" and Client Secret" variables with your own, which can be obtained at Spotify for Developers: https://developer.spotify.com/

Then you can simply run the command `python main.py "[Insert Song Name Here]" "[Insert Artist Name Here]"`. Make sure to put the song name in quotes. It is best to open Spotify and find the song first so you can enter its name exactly as it appears in Spotify.

# Things to look out for
Spaces: For songs with a space in them, you must put the song name in quotes, if you don't, the script will take each word as a seperate argument and will not be able to find the song.

### Older Songs/Remasters
Some older songs may have Remastered somewhere in the title, if this is not added the script will not find the song. For example, take "Bennie and the Jets" by Elton John. If you type "Bennie and the Jets" as the argument, but Spotify calls the song "Bennie and the Jets - 2014 Remastered", the script will not be able to find the song. Make sure to look at the song in Spotify and then copy the exact title as the argument for this script.

### Artist Features
Some songs also feature select artists and put their name in the title in parenthesis using feat. or ft. For example, take "See You Again" by Wiz Khalifa. If you type "See You Again" as the argument, but Spotify calls the song "See You Again (feat Charlie Puth)", the script will not be able to find the song. Remember to watch out for these as well, as they are technically part of the song title and must be included in the argument.

### Case sensitive
Remember to capitalize song names however they are capitalized in the Spotify title.