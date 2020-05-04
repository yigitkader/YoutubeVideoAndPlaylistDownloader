from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm



import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()






# https://www.youtube.com/watch?v=II8V0_ilRbU&list=PLdJYl6XU45uLIHaPBQEj-cEMynAl0oeiz

print("Video linkini giriniz : ")
link = input()

try:
    pl = Playlist(link)
    countVideos = len(pl.populate_video_urls())
except:
    yt = YouTube(link)
    countVideos = 0


if countVideos >= 2:
    allLinks = []
    for i in pl.populate_video_urls():
        allLinks.append(i)

    for link in tqdm(allLinks):
        yt = YouTube(link)
        video = yt.streams.first()
        video.download()

else:
    yt = YouTube(link)
    video = yt.streams.first()
    video.download()

