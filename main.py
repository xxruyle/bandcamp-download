import bandcampdl 
import sys
sys.stdout.reconfigure(encoding='utf-8')  # Fixes git bash crashes

# Customize the main function however you like by using the methods found in objects.py

# This main() function downloads songs taken from bandcamp and adds the corresponding metadata to each one
def main():
    link = input("Enter Bandcamp link: ")
    dl = bandcampdl.downloader(link, bandcampdl.PATH)
    dl.download()

if __name__ == "__main__":
    main()