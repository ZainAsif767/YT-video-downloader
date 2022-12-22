# you need to imprt pytube library using --> pip install pytube (on TERMINAL)
from pytube import YouTube
url = input("Video URL: >")
yt = YouTube(url)

stream = yt.streams.first()
stream.download()  # this will download in your current working directory
