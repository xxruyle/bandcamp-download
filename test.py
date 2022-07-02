#File for testing functions 
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

def badchar(string):  # Removes illegal filename characters 
    for c in '\/:*?"<>|':
        string = string.replace(c,'-')
    return string;

def cleanString(string):  # removes illegal unicode characters from track name
    list = []
    for letter in string:
        if letter.isalnum() or letter == ' ' or letter == '(' or letter == ')' or letter == "," or letter == ".":
            list.append(letter)
        else:
            list.append("")
    return ''.join(list).strip()


title = badchar("Cherry Bay 🍒")
print(len(cleanString(title)))

