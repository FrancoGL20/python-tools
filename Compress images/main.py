import dotenv
import tinify
import os
from sys import exit


#* Load environment variables
dotenv.load_dotev()
tinify.key = os.getenv("TINIFY_API_KEY")


#* Get the input and output directories
INPUT_DIRECTORY = input("Enter the directory where the photos are located [default: photos]: ")

# if no folder is specified, use the default folder (photos)
if not INPUT_DIRECTORY:
    INPUT_DIRECTORY = "./photos"

# verify if the input directory exists
if not os.path.exists(INPUT_DIRECTORY):
    print("The specified directory does not exist")
    exit(1)


OUTPUT_DIRECTORY = input("Enter the directory where the compressed photos will be saved [default: output]: ")

# if no folder is specified, use the default folder (output)
if not OUTPUT_DIRECTORY:
    OUTPUT_DIRECTORY = "./output"

# verify if the output directory exists and create it if it doesn't
if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)


#* Compress the photos
counter = 0
total_photos_count = len(os.listdir(INPUT_DIRECTORY))

for photo in os.listdir(INPUT_DIRECTORY):
    source = tinify.from_file(os.path.join(INPUT_DIRECTORY, photo))
    source.to_file(os.path.join(OUTPUT_DIRECTORY, photo))
    counter += 1
    print(f"Processed {counter}/{total_photos_count} photos, {photo}")