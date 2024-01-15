import dotenv
import os
import signal
import sys

def handler(signum, frame):
    """
    Function that handles the interruption signal (ctrl+c) and deletes the .cache and download_list.log files if they exist.

    Args:
    - signum: signal number
    - frame: current stack frame
    """
    
    print("Playlist downloaded has been stopped",end="")
    
    if os.path.exists(".cache"):
        os.remove(".cache")
        print(", the .cache file has been deleted",end="")

    if os.path.exists("./playlists/download_list.log"):
        os.remove("./playlists/download_list.log")
        print(", the download_list.log file has been deleted")
    
    # finish the program
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

# Load environment variables
dotenv.load_dotenv()

# Get environment variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Add temporal environment variables, these will be deleted when the program ends
os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret

playlist_link = input("Enter the playlist link: ")

# Verify if the playlist directory exists
if not os.path.exists("./playlists"):
    os.mkdir("./playlists")

# Execute the spotify_dl command
# os.system(f"spotify_dl -l {playlist_link} -o \"./playlists/\" -s y") # Make use of SponsorBlock
os.system(f"spotify_dl -l {playlist_link} -o \"./playlists/\"")

