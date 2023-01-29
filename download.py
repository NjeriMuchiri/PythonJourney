import pytube #library for downloading the videos

url = input("Enter the video url: ")

path="/home/muchirinjeri/Downloads"

#magic line to download the video

pytube.YouTube(url).streams.get_highest_resolution().download(path)
