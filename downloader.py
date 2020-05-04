from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm


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

