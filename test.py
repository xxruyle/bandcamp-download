#File for testing functions 
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

def badchar(self, string):  # Removes illegal filename characters 
        for c in '\/:*?"<>|':
            string = string.replace(c,'-')
        return string;


ytmusic = YTMusic("headers_auth.json")

