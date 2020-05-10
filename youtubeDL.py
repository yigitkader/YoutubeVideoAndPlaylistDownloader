from pytube import Playlist
from pytube import YouTube
from tqdm import tqdm


def downloadVideo(url):
    yt = YouTube(url)
    #higher resolution
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download()

    #YouTube(url).streams.first().download()

def downloadPlaylist(url):
    pl = Playlist(url)
    #pl.download_all()
    allLinks = []
    for i in pl.video_urls:
        allLinks.append(i)

    for link in tqdm(allLinks):
       downloadVideo(link)




print("[+] Tek video icin 1")
print("[+] Playlist icin 2")
select = int(input())

print("Video Linki :")
url = input()
print("İndirme işleminiz başlıyor..")
print()

if select == 1 and url != "":
    downloadVideo(url)

elif select == 2 and url != "":
    downloadPlaylist(url)

else:
    print("! Hata")