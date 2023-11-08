# Download music from Spotify

## Modules used (and documentation)

- [spotify_dl](https://github.com/SathyaBhat/spotify-dl)

## Requirements

1. Python 3.7 or higher (preferably)
2. ffmpeg
    - For linux:
        ```bash
        sudo apt-get install -y libav-tools
        ```
    - For Windows:
        1. Download ffmpeg from [here](https://github.com/BtbN/FFmpeg-Builds/releases)
        2. Extract the zip file
        3. Move the unzipped folder to `C:\Program Files\` or a folder of your choice
        4. Add the path to the `bin` folder to the `PATH` environment variable
3. Spotify account
   1. Create an aplication in [Spotify for Developers](https://developer.spotify.com/dashboard/applications)
   2. Copy the Client ID and the Client Secret

## Creation of the virtual environment and installation of the modules

```bash
python -m venv env
.\env\Scripts\activate # (Windows)
# source env/bin/activate (Linux)

pip install -r requirements.txt
```

## Use 

### Use with the [main.py](main.py) script

1. Configure the values for the environment variables SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET with the values copied from Spotify for Developers into a file named `.env` with the following format:
    ```bash
    SPOTIPY_CLIENT_ID="your-spotify-client-id"
    SPOTIPY_SECRET_ID="your-spotify-client-secret"
    ```
2. Run the script
    ```bash
    python main.py
    ```
3. It will ask you for the playlist url
4. The downloaded songs will be saved in the `playlists` folder

NOTE: In case the execution of the script is interrupted (ex: ctrl+c), the `.cache` and `download_list.log` files will be deleted to avoid errors in the next execution.

### Use directly from the terminal

1. Configure the environment variables SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET with the values copied from Spotify for Developers
   - Linux:
       ```bash
       export SPOTIPY_CLIENT_ID=your-spotify-client-id
       export SPOTIPY_CLIENT_SECRET=your-spotify-client-secret
       ```
   - Windows Powershell:
       ```powershell
       $env:SPOTIPY_CLIENT_ID=your-spotify-client-id
       $env:SPOTIPY_CLIENT_SECRET=your-spotify-client-secret
       ```
   - Windows CMD:
       ```cmd
       set SPOTIPY_CLIENT_ID=your-spotify-client-id
       set SPOTIPY_CLIENT_SECRET=your-spotify-client-secret
       ```

3. Execute the script using `spotify_dl`. for more information about the input parameters, execute `spotify_dl --h`
    
    For most cases, you can use the following command:
    ```bash
    spotify_dl -l <playlist_url> -o <output_dir>
    ```
    To download multiple playlists, you can use the following command:
    ```bash
    spotify_dl -l <playlist_url_1> <playlist_url_2> ... <playlist_url_n> -o <output_dir>
    ```
    To use SponsorBlock (to skip ads), you can use the following command:
    ```bash
    spotify_dl -l <playlist_url> -o <output_dir> -s y
    ```
    To ensure parallel download, you can use the following command: (where `<number>` is the number of cores to use)
    ```bash
    spotify_dl -l <playlist_url> -o <output_dir> -mc <number>
    ```


3. In case you want to configure default parameters, you can create a `~/.spotify_dl_settings` file with the following format:
    ```json
    {
        "output_dir": "path/to/output/dir",
        "verbose": false,
        "overwrite": true,
        "format": "mp3",
        "quality": "320k",
        "download_only_metadata": false,
        "download_cover_image": true,
        "download_lyrics": false,
    }
    ```

## Credits

- GitHub repository [SathyaBhat](https://github.com/SathyaBhat/spotify-dl)