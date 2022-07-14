# bandcamp-download
Simple python script which downloads Bandcamp albums and songs in mp3 format. MP3 Files come with ID3 metadata. 


# The Script in Action
### Running the script
```bash
$ bcdl https://wolfgang-amadeus-mozart.bandcamp.com/album/mozarts-requiem-instrumental
Getting MP3 links...
Getting album cover from: https://f4.bcbits.com/img/a2608013838_16.jpg
Downloading Album: Mozarts Requiem  Instrumental: 100%|██████████████████████████████████████████| 12/12 [00:05<00:00,  2.06it/s] 100%|████████████████████████████████████████████████████████████████████████████████████████████| 12/12 [00:05<00:00,  2.06it/s] Download Success!
```

### The mp3 files and album cover downloaded with correct metadata
<img src='images\album.png'></img>

### Example of uploading to YoutTube Music using <a href="https://github.com/sigma67/ytmusicapi">ytmusicapi</a> 
```powershell
Folder C:/Music/Mozarts Requiem Instrumnetal: 100%|██████████████████████████████████████████████████████| 13/13 [00:21<00:00,  1.68s/it]
Upload Success!
```

# Setup
Supports Python 3.8.8 or higher

1) Install the project zip 

2) Install the requirements in the project directory

```powershell
pip install -r requirements.txt
```

1) Set your preferred directory path where you want your music installed to  `.\bandcampdl\pathdir.py`  

```python
MUSIC_DIRECTORY = "C:\Music"  # Default directory
```

1) run `python main.py [-h] [-u] link` 

```powershell 
usage: main.py [-h] [-u] link

Download bandcamp albums

positional arguments:
  link          Enter a valid bandcamp album or song link

optional arguments:
  -h, --help    show this help message and exit
  -u, --upload  Uploads files to YT Music
```

6) New album or song folder will now be where you set ```MUSIC_DIRECTORY```

# Uploading to Youtube Music
The script supports  <a href="https://github.com/sigma67/ytmusicapi">ytmusicapi</a> where you can instantly upload songs to Youtube Music after downloading.

1) Follow the setup steps using the <a href="https://ytmusicapi.readthedocs.io/en/latest/setup.html">ytmusicapi documentation</a> to create a `headers_auth.json`
  
2) Place the newly created `headers_auth.json` in the directory folder 
   
  
3) Use the `--upload` argument when running `python main.py`

# Further Notes
- Yes, bandcamp allows people to download <a href="https://get.bandcamp.help/hc/en-us/articles/360007902173-I-heard-you-can-steal-music-on-Bandcamp-What-are-you-doing-about-this-">the underlying MP3-128 files</a>

- Support bandcamp artists!
