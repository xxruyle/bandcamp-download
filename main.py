import bandcampdl 
import sys

sys.stdout.reconfigure(encoding='utf-8')  # Fixes git bash crashes

# Customize the main function however you like by using the methods found in objects.py or youtube_music.py

# This main() function downloads songs taken from bandcamp and adds the corresponding metadata to each one
def main():
    ''' Customize the main function however you like by using the methods found in objects.py or youtube_music.py 
        This main() function downloads songs taken from bandcamp and adds the corresponding metadata to each one.
        
        It also can upload the songs to YTMusic if  ytmusicapi setup is followed.
    '''

    link = input("Enter Bandcamp link: ")
    dl = bandcampdl.downloader(link, bandcampdl.PATH)

    # dl.download downloads the songs from the inputted link 
    album_folder = dl.download()    

    # Remove this if you do not want to upload songs to YT Music 
    #u1 = bandcampdl.YTM_upload()
    #u1.upload_songs(album_folder)
    

if __name__ == "__main__":
    main()