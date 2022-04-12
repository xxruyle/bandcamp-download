# bandcamp-download
Script which downloads Bandcamp albums and songs in mp3 format. MP3 Files come with ID3 metadata. 

The downsides of downloading mp3s off the internet instead of using a mainstream music player is no more! ID3 Album cover, title, year, album artist... bandcamp-download will take care of it!

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

...
```

### The mp3 files and album cover downloaded
<img src='images\album.png'></img>

### Correct ID3 metadata
<p align='center'><img src='images\metadata.png' width='500' height='376.08'/>

# Setup
1) Install the project zip and extract it. Call it bandcampdownload
2) Create a virtualenv if needed

```powershell
py -m venv env

.\env\Scripts\activate
```

3) Go to the project directory and enter:

```powershell
pip install -r requirements.txt
```

4) Set your preferred directory where you want your music installed in  `.\bandcampdl\pathdir.py`  

```python
MUSIC_DIRECTORY = "C:\Music"  # Default directory
```

5) run `main.py`

```powershell 
cd .\bandcampdownload\

python main.py
```
6) Enter the bandcamp link containing the song or album you want to install
7) New album or song folder will now be where you set ```MUSIC_DIRECTORY```

# To Do
✅ Download the album cover to directory folder alongside the MP3s 

✅ Fix how album names with illegal characters cannot be added to the directory 

✅ Add Mutagen support 

✅ requirements.txt

☐ Error handling 

☐ PyPi

☐ GUI

# Credits
- Made for educational purposes 

- Support bandcamp artists!
