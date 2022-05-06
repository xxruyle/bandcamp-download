from ytmusicapi import YTMusic
from os import listdir 

class YTM_upload():
    '''Class which deals with YT Music api uploads'''
    def __init__(self):
        self.ytmusic = YTMusic("headers_auth.json")  # Place the path to your headers_auth.json here

    def upload_songs(self, album_folder):
        for song in listdir(album_folder):  
            if ".mp3" in song:  # Makes sure non mp3 files do not get uploaded
                print(f"Uploading... {song}")
                self.ytmusic.upload_song(f"{album_folder}/{song}")

        print("Success!")

