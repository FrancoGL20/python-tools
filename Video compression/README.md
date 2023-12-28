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
# source env/bin/activate (Linux)

python -m pip install --upgrade pip

pip install -r requirements.txt
```

