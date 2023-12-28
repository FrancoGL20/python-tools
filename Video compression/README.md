# Video compression with ffmpeg and python

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

## Creation of the virtual environment and installation of the modules

```bash
python -m venv env

.\env\Scripts\activate # (Windows)
# source env/bin/activate # (Linux)

python -m pip install --upgrade pip

pip install -r requirements.txt
```

## Use

1. Move the input video to the current directory
2. Into the line `file_name = compress_video('INPUT_VIDEO_NAME', OUTPUT_VIDEO_SIZE * 1024)` change the `INPUT_VIDEO_NAME` for the name of the input video and the `OUTPUT_VIDEO_SIZE` for the desired maximum size of the output video in MB
3. Run the script
    ```bash
    python main.py # (Windows)
    # python3 main.py # (Linux)
    ```
4. The output video will be saved in the `output` directory with the same name as the input video with the suffix `_compressed`

## Credits

- Github Gist from [ESWZY](https://gist.github.com/ESWZY/a420a308d3118f21274a0bc3a6feb1ff)