# bandcamp-download
Download Bandcamp albums and songs in mp3 format. MP3 Files come with ID3 metadata. The downsides of downloading mp3s off the internet instead of using a mainstream music player is no more! ID3 Album cover, title, year, album artist... bandcamp-download will take care of it!

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

5) run `__main__.py`

```powershell 
cd .\directory the project is in\

python bandcampdownload
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
