import bandcampdl 
# Customize the main function however you like by using the methods found in objects.py

# This main() function downloads songs taken from bandcamp and adds the corresponding metadata to each one
def main():
    link = input("Enter Bandcamp link: ")
    dl = bandcampdl.downloader(link, bandcampdl.PATH)
    dl.download()

if __name__ == "__main__":
    main()