import os
import subprocess

from pytube import Playlist, YouTube

def run(pl):
    # get parent directory; VERY IMPORTANT!!
    # INCLUDE LAST SLASH AFTER FOLDER NAME
    # e.g. /home/username/Folder/ or C:\Users\Username\Folder\
    filepath = input("Please enter the filepath of the directory where this script is located:\n")
    # get linked list of links in the playlist
    links = pl.video_urls
    # download each item in the list
    for l in links:
        # converts the link to a YouTube object
        yt = YouTube(l)
        # takes first stream; since ffmpeg will convert to mp3 anyway
        music = yt.streams.first()
        # gets the filename of the first audio stream
        default_filename = music.default_filename
        print("Downloading " + default_filename + "...")
        # downloads first audio stream
        music.download()
        # creates mp3 filename for downloaded file
        # adjust the length of the downloaded video extension
        # example, .3gpp = [0:-4]
        new_filename = default_filename[0:-4] + "mp3"
        print("Converting to mp3....")
        # converts mp4 audio to mp3 audio
        subprocess.run(['ffmpeg', '-i', 
            os.path.join(filepath, default_filename),
            # used 192kbps
            '-b:a', '192K',
            os.path.join(filepath, new_filename)
        ])
    
    print("Download finished.")

if __name__ == "__main__":
    url = input("Please enter the url of the playlist you wish to download: ")
    pl = Playlist(url)
    run(pl)
