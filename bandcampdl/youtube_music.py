from ytmusicapi import YTMusic
from os import listdir 
from tqdm import tqdm 
import time 

class YTM_upload():
    '''
    Class which deals with YT Music api uploads
    :param headers_path: the path to the headers_auth.json required to initialize ytmusicapi
    '''
    def __init__(self, headers_path):
        self.ytmusic = YTMusic(headers_path)  # Place the path to your headers_auth.json here

    def upload_songs(self, album_folder):
        '''
        Uploads an entire folder of songs downloaded from bandcamp to youtube music
        :param album_folder: the folder that the downloaded songs are located in 

        :example:
        >>> upload_songs("C:\Music\myAlbum")
        :returns: Song1.mp3 Upload Result: STATUS_SUCCEED
        ... 
        '''
        for song in tqdm(listdir(album_folder), desc=f"Uploading Folder {album_folder}", leave=True):  
            if song[-4:] == ".mp3":  # Makes sure non mp3 files do not get uploaded
                upload_status = str(self.ytmusic.upload_song(f"{album_folder}/{song}"))

                #If a response error occurs, the script will wait 20 seconds
                if upload_status == "<Response [503]>" or upload_status == "<Response [409]>":
                    upload_error = True 
                    while upload_error:
                        print("\nWaiting 20 seconds due to rate limit...")
                        time.sleep(20)
                        upload_status = self.ytmusic.upload_song(f"{album_folder}/{song}")
                        if str(upload_status) == "STATUS_SUCCEEDED":
                            upload_error = False
                
        print("Upload Success!")
