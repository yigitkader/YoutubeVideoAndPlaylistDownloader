from pytube import Playlist
from pytube import YouTube
from tqdm import tqdm


def downloadVideo(url):
    try:
        yt = YouTube(url)
        
        yt.streams.get_highest_resolution().download()

        #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()

    except :
        print("A problem occured while dowloading video")


def downloadPlaylist(url):
    try:
        pl = Playlist(url)

        for video in tqdm(pl):
            video.streams.get_highest_resolution().download()
            
    except :
        print("A problem occured while dowloading playlist")

print("[+] Tek video icin 1")
print("[+] Playlist icin 2")
select = int(input())

print("Video Linki :")
url = input().strip()
print("İndirme işleminiz başlıyor..")
print()

if select == 1 and url != "":
    downloadVideo(url)

elif select == 2 and url != "":
    downloadPlaylist(url)

else:
    print("! Hata")