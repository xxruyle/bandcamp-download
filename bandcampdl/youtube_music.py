from ytmusicapi import YTMusic
from os import listdir 
import time 

class YTM_upload():
    '''Class which deals with YT Music api uploads'''
    def __init__(self):
        self.ytmusic = YTMusic("headers_auth.json")  # Place the path to your headers_auth.json here

    def upload_songs(self, album_folder):
        for song in listdir(album_folder):  
            if ".mp3" in song:  # Makes sure non mp3 files do not get uploaded
                upload_status = str(self.ytmusic.upload_song(f"{album_folder}/{song}"))
                print(song + " Upload Result: " + upload_status)

                #If a response error occurs, the script will wait 11 seconds
                while "<Response" in upload_status:
                    print("Waiting 10 seconds...")
                    time.sleep(11)
                    upload_status = self.ytmusic.upload_song(f"{album_folder}/{song}")
                    print(song + " Upload Result: " + str(upload_status))
                
        # rechecking to see if every song was uploaded       
        #browse_id = self.ytmusic.get_library_upload_albums()[0]["browseId"] 
        #self.ytmusic.get_library_upload_album(browse_id)["tracks"]


        print("Upload Success!")

