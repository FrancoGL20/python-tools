# Descargar música de Spotify

## Requisitos

1. Python 3.7 o superior
2. ffmpeg
    - Para linux:
        ```bash
        sudo apt-get install -y libav-tools
        ```
    - Para Windows:
        ```bash
        winget install ffmpeg
        ```
3. Cuenta en Spotify
   1. Crear una aplicación en [Spotify for Developers](https://developer.spotify.com/dashboard/applications)
   2. Copiar el Client ID y el Client Secret

## Creación de entorno virtual e instalación de librerias

```bash
python3 -m venv env
.\env\Scripts\activate # (Windows)
# source env/bin/activate (Linux)

pip install -r requirements.txt
```

## Uso

1. Configurar las variables de entorno SPOTIPY_CLIENT_ID y SPOTIPY_CLIENT_SECRET con los valores copiados de Spotify for Developers
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

2. Ejecutar el script usando `spotify_dl`. para más información sobre los parámetros de entrada, ejecutar `spotify_dl --h`
    
    Para la mayoría de los casos, se puede usar el siguiente comando:
    ```bash
    spotify_dl -l <playlist_url> -o <output_dir>
    ```
    Para descargar multiples playlists, se puede usar el siguiente comando:
    ```bash
    spotify_dl -l <playlist_url_1> <playlist_url_2> ... <playlist_url_n> -o <output_dir>
    ```
    Para utilizar SponsorBlock, se puede usar el siguiente comando:
    ```bash
    spotify_dl -l <playlist_url> -o <output_dir> -s y
    ```
    Para asegurar la descarga en paralelo, se puede usar el siguiente comando: (donde `<number>` es la cantidad de nucleos a utilizar)
    ```bash
    spotify_dl -l <playlist_url> -o <output_dir> -mc <number>
    ```


3. En caso de querer configurar parametros por defaults se puede crear un archivo `~/.spotify_dl_settings` con el siguiente formato:
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

## Créditos

- Respositorio de GitHub [SathyaBhat](https://github.com/SathyaBhat/spotify-dl)