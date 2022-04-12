from bs4 import BeautifulSoup
import requests 
import urllib.request
import os 


class linkfinder:  
    '''finds the links which contain bandcamp mp3s'''
    def __init__(self, link):
        self.link = link
        self.album_length = None 

    def get_html(self):
        response = requests.get(self.link).content 
        soup = BeautifulSoup(response, 'html.parser')
        return soup

    def get_script(self):
        response = requests.get(self.link)
        url = response.content
        soup = BeautifulSoup(url, 'html.parser')
        links = soup.find_all("script")
        return links 

    def get_links(self):
        link_list = []  # list of all the song links 
        for link in self.get_script():
            if "https://t4.bcbits.com/stream" in str(link): 
                if "&quot;mp3-128&quot;:&quot;" in str(link):  # &quot;mp3-128&quot;:&quot; is one possible line before the song link
                    splt = str(link).split('&quot;mp3-128&quot;:&quot;')
                    for j in range(len(splt)):
                        song_link = splt[j].split(';}')[0]
                        link_list.append(song_link)
                    link_list.pop(0)

                elif '{"mp3-128":' in str(link):  # another possible entry before the song link
                    splt = str(link).split('{"mp3-128":')
                    for j in range(len(splt)):
                        song_link = splt[j].split('}')[0]
                        link_list.append(song_link)
                    link_list.pop(0)

        self.album_length = len(link_list)

        return link_list
        

class meta_info(linkfinder):  
    '''finds the metadata info for songs, album cover, arist name, release date'''
    def __init__(self, link):
        super().__init__(link)
        self.soup = linkfinder.get_html(self)

    def badchar(self, string):  # Removes illegal characters 
        for c in '\/:*?"<>|':
            string = string.replace(c,'')
        return string;

    def get_title(self):  # gets the album or song title 
        init_title = self.soup.find('h2', class_="trackTitle").text.strip()
        title = self.badchar(init_title)
        return title 

    def get_artist(self):  # Gets the artist's name  
        container = self.soup.find('div', attrs={"id": "name-section"})
        artist = container.find('a').text
        return artist 

    def get_cover(self):  # Gets the image link of the album cover 
        container = self.soup.find('a', class_="popupImage")
        image = container.find('img')
        cover = image.get('src')
        return cover 

    def get_trackname(self):  # Gets the names of the track and the track number in a dictionary 
        trackinfo = {}  # "Name" : "Track Number"
        container = self.soup.find_all('tr', class_="track_row_view linked")
        j = 1
        for i in container:
            init_track = i.find('span', class_='track-title').text.strip()
            track = self.badchar(init_track)  # removes potential bad characters from track name 
            trackinfo[track] = j
            j += 1
        return trackinfo

    def get_release(self):  # Gets the year the album/track was released 
        string = self.soup.find('div', class_="tralbumData tralbum-credits").text.strip()
        date = string.replace('released ', '')
        year = date[-4:]
        return year # This returns the year but we can also return the date if we want 

 

class downloader(meta_info):  
    '''downloads the mp3 of every link in the song_list '''
    def __init__(self, link, directory):
        super().__init__(link)
        self.directory = f'{directory}\{meta_info.get_title(self)}'
        self.download_list = linkfinder.get_links(self)
        

    def download(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        else:
            print(f'{self.directory} already exists ')

        print("Downloading...")
        for i in range(len(self.download_list)):
            track = self.download_list[i].strip('"')
            response = requests.get(track)
            print(f"Downloading... {list(meta_info.get_trackname(self))[i]} ")
            with open(f'{self.directory}\{list(meta_info.get_trackname(self))[i]}.mp3', 'wb') as f:  # installing the song  to the intended directory 
                f.write(response.content)

        print(f'Getting album cover from: {meta_info.get_cover(self)}')
        with open(f'{self.directory}\cover.jpg', 'wb') as f:  # adding album cover to album/song directory folder
            cover_response = requests.get(meta_info.get_cover(self))
            f.write(cover_response.content)

        print("Success!")



