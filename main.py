import bandcampdl 
import sys
import argparse 

sys.stdout.reconfigure(encoding='utf-8')  # Fixes git bash crashes

# Customize the main function however you like by using the methods found in objects.py or youtube_music.py

# This main() function downloads songs taken from bandcamp and adds the corresponding metadata to each one
def main(link):
    ''' Customize the main function however you like by using the methods found in objects.py or youtube_music.py 
        This main() function downloads songs taken from bandcamp and adds the corresponding metadata to each one.
        
        It also can upload the songs to YTMusic if  ytmusicapi setup is followed.
    '''

    dl = bandcampdl.downloader(link, bandcampdl.PATH)

    # dl.download downloads the songs from the inputted link 
    album_folder = dl.download()    

    # Remove this if you do not want to upload songs to YT Music 
    if args.upload:
        u1 = bandcampdl.YTM_upload(bandcampdl.HEADERS_AUTH)
        u1.upload_songs(album_folder)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Download bandcamp albums")
    parser.add_argument("link", metavar="link", type=str, help = "Enter a valid bandcamp album or song link")
    parser.add_argument("-u", "--upload", action="store_true", help="Uploads files to YT Music")
    parser.set_defaults(feature=False)
    args = parser.parse_args()
    main(args.link)