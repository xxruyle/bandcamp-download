#File for testing functions 
import requests
from bs4 import BeautifulSoup

string = "//"

print(string.isalnum())

def badchar(self, string):  # Removes illegal filename characters 
        for c in '\/:*?"<>|':
            string = string.replace(c,'-')
        return string;