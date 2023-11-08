import dotenv
import os
import signal

def handler(signum, frame):
    print("Se ha detenido la descarga de la playlist",end="")
    
    # si existe el archivo .cache lo elimina
    if os.path.exists(".cache"):
        os.remove(".cache")
        print(", se ha eliminado el archivo .cache",end="")
    
    if os.path.exists("./songs/download_list.log"):
        os.remove("./songs/download_list.log")
        print(", se ha eliminado el archivo download_list.log")
    
    exit(0)

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

# Ejecutar el comando para descargar la playlist
os.system(f"spotify_dl -l {playlist_link} -o \"./songs/\" -s y")

