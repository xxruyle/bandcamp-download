import bandcampdownload 

def main():
    link = input("Enter Bandcamp link: ")
    dl = bandcampdownload.downloader(link, bandcampdownload.PATH)
    dl.download()

if __name__ == "__main__":
    main()