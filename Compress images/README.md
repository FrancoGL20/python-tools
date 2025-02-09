# Compression of images

## Requirements

1. Python 2.7 or higher (preferably)
2. An account and API key from [TinyPNG](https://tinypng.com/developers)

<br>

## Creation of the virtual environment and installation of the modules

```bash
python -m venv env
.\env\Scripts\activate # (Windows)
# source env/bin/activate (Linux)

python -m pip install --upgrade pip

pip install -r requirements.txt
```

<br>

## Use

1. Configure the values for the environment variable TINYPNG_API_KEY with the value copied from TinyPNG into a file named `.env` with the following format:
    ```bash
    TINYPNG_API_KEY="your-tinypng-api-key"
    ```
2. Run the script
    ```bash
    python main.py
    ```
3. It will ask you for two paths:
    - The path to the folder with the images to compress 
        
        **Note**: this can be empty and the program will use the photos directory

    - The path to the folder where the compressed images will be saved 
    
        **Note**: this can be empty and the program will use the output directory

4. The compressed images will be saved in the folder specified in step 3

<br>

## Credits

- [TinyPNG](https://tinypng.com/)