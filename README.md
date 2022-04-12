# bandcamp-download
Download Bandcamp albums and songs in mp3 format.

# Setup
1) Install the project zip
2) Create a virtualenv if needed

```powershell
py -m venv env

.\env\Scripts\activate
```

3) Go to the project directory and enter:

```powershell
pip install -r requirements.txt
```

4) Set your preferred directory where you want your music installed in the pathdir.py  

```python
MUSIC_DIRECTORY = "C:\Music"  # Default directory
```

5) run main.py

```powershell 
python main.py 
```
6) Enter the bandcamp link containing the song or album you want to install
7) New album or song folder will now be where you set ```MUSIC_DIRECTORY```

# To Do
✅ Download the album cover to directory folder alongside the MP3s 

✅ Fix how album names with illegal characters cannot be added to the directory 

☐ Add Mutagen support 

☐ Error handling 

☐ exe file 

☐ GUI

# Credits
- Made for educational purposes 

- Remember to support artists 
