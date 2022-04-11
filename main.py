from ast import get_source_segment
from re import I
from objects import linkfinder, downloader, meta_info
from dotenv import load_dotenv
import os 

load_dotenv()
MUSIC_DIRECTORY = os.getenv("MUSIC_DIRECTORY")

def main():
    link = input("Enter Bandcamp link: ")
    dl = downloader(link, MUSIC_DIRECTORY)
    dl.download()

if __name__ == "__main__":
    main()