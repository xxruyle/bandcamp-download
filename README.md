# bandcamp-download
Simple script which downloads Bandcamp albums and songs in mp3 format. MP3 Files come with ID3 metadata. 

Uses <a href="https://github.com/sigma67/ytmusicapi">ytmusicapi</a> to instantly upload songs to Youtube Music after downloading.


# The Script in Action
### Running the script
```powershell
(base) PS C:\coding\bandcampdownload> python main.py
Enter Bandcamp link: https://wolfgang-amadeus-mozart.bandcamp.com/album/mozarts-piano-sonatas-vol-1
Getting MP3 links...
Getting album cover from: https://f4.bcbits.com/img/a3050325896_16.jpg
Downloading...
Downloading... Piano Sonata No.1 in C-Major, K. 279- I. Allegro 
Downloading... Piano Sonata No.1 in C-Major, K. 279- II. Andante 
Downloading... Piano Sonata No.1 in C-Major, K. 279- III. Allegro 
Downloading... Piano Sonata No.2 in F-Major, K. 280- I. Allegro Assai 
Downloading... Piano Sonata No.2 in F-Major, K. 280- II. Adagio 
Downloading... Piano Sonata No.2 in F-Major, K. 280- III. Presto 
Success!
...
```

### The mp3 files and album cover downloaded
<img src='images\album.png'></img>

### Correct ID3 metadata
<p align='center'><img src='images\metadata.png' width='500' height='376.08'/>

### Uploading to YoutTube Music using <a href="https://github.com/sigma67/ytmusicapi">ytmusicapi</a>
```powershell
Uploading... Piano Sonata No.1 in C-Major, K. 279- I. Allegro 
Uploading... Piano Sonata No.1 in C-Major, K. 279- II. Andante 
Uploading... Piano Sonata No.1 in C-Major, K. 279- III. Allegro 
Uploading... Piano Sonata No.2 in F-Major, K. 280- I. Allegro Assai 
Uploading... Piano Sonata No.2 in F-Major, K. 280- II. Adagio 
Uploading... Piano Sonata No.2 in F-Major, K. 280- III. Presto 
Success!
```

# Setup
1) Install the project zip 
2) Create a virtualenv if needed

3) Install the requirements in the project directory

```powershell
pip install -r requirements.txt
```

4) Set your preferred directory where you want your music installed in  `.\bandcampdl\pathdir.py`  

```python
MUSIC_DIRECTORY = "C:\Music"  # Default directory
```

5) run `main.py` and enter a bandcamp link 

```powershell 
python main.py
```

6) New album or song folder will now be where you set ```MUSIC_DIRECTORY```

# Uploading to Youtube Music 
1) Follow the setup steps to setup using the <a href="https://ytmusicapi.readthedocs.io/en/latest/setup.html">ytmusicapi documentation</a>
  
2) Enter the `headers_auth.json` path into YTMusic class in `youtube_music.py` 

3) Use the `upload_music()` method in `youtube_music.py`

# To Do
✅ Download the album cover to directory folder alongside the MP3s 

✅ Fix how album names with illegal characters cannot be added to the directory 

✅ Add Mutagen support 

✅ requirements.txt

✅ Error handling 

✅ YouTube Music Upload using ytmusicapi 

- [ ] Refactoring
  



# Credits
- [ytmusicapi](https://github.com/sigma67/ytmusicapi)
- Made for educational purposes 

- Support bandcamp artists!
