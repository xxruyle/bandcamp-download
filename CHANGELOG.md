# Change Log 

## v2.0.0 - July 13, 2022
#### tqdm 
- Contains all changes and bugfixes from 1.0.1-1.0.3
- tqdm support 

## v1.0.3 
#### Unicode 
- Fixed problem where extra whitespaces would appear in folder names 

## v1.0.2 
#### Argparse

- argparse support
- Fixed an <a href="https://github.com/sigma67/ytmusicapi/issues/6">upload issue</a> where uploading albums with around or more than ~13 songs caused a response error. 
- Added publisher metadata with the get_publisher() method in meta_info
- Added comments to objects.py and youtube_music.py 
- Disabled the ability for downloader.download() to download a bandcamp album even if the folder already existed

## v1.0.1 - May 5, 2022
#### YouTube music upload support

- ytmusicapi support
- upload_songs() method in youtube_music.py 


# v1.0.0 - April 23, 2022
#### Initial release 

- Added ability to download the album cover to directory folder alongside the MP3s 

- Fix how album names with illegal characters cannot be added to the directory 

- Added Mutagen support 

- Added requirements.txt

- Added Error handling 



