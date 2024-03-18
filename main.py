from pytube import YouTube
import os

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")

    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution
    yd = yt.streams.get_highest_resolution()

    # change current directory
    os.chdir("C:/Users/User/Videos/yt")

    # Download the video to the current directory
    yd.download()

    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))