#@Author Yigit Kader

import os
import sys


from pytube import YouTube
from pytube import Playlist


print("[+] Tek video indirmek icin -> 1 ")
print("[+] Playlist  indirmek icin -> 2 ")
choise = int(input())


for i in tqdm(range(1,1000)):
    if choise == 1:
        print("[+] İndirmek istedigin videonun linkini giriniz : ")
        videoLink = input()
        YT = YouTube(videoLink)
        stream = YT.streams.first()
        stream.download()
    elif choise == 2:
        print("[+] İndirmek istedigin Playlistin linkini giriniz : ")
        playlistLink = input()
        PL = Playlist(playlistLink)
        PL.download_all()

