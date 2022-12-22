# Download YouTube videos in python

import pytube

video_url = input("Enter the URL of the YouTube video: ")

yt = pytube.YouTube(video_url)

for i, stream in enumerate(yt.streams):
    print(f"{i}: {stream.resolution}")

resolution = int(
    input("Enter the number of the video resolution you want to download: "))

video = yt.streams[resolution]

video.download()

print("Video downloaded successfully! Please check the video in your Download Folder")
