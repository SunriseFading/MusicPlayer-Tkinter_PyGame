import tkinter as tk
import pygame
from tkinter.filedialog import askdirectory
from os import chdir, listdir

def GetSongList():
    directory = askdirectory()
    chdir(directory)
    return listdir()

music_player = tk.Tk()
music_player.title("Music")
music_player.geometry("400x400")

s_list = GetSongList()
play_list = tk.Listbox(music_player, selectmode=tk.SINGLE)

for i in s_list:
    pos = 0
    play_list.insert(pos, i)
    pos += 1

pygame.init()
pygame.mixer.init()

class MediaControl:
    def Load():
        pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    def Play():
        MediaControl.Load()
        var.set(play_list.get(tk.ACTIVE))
        pygame.mixer.music.play()

    def Stop():
        pygame.mixer.music.stop()

    def Pause():
        pygame.mixer.music.pause()

    def Unpause():
        pygame.mixer.music.unpause()

Button1 = tk.Button(music_player, width=5, height=3, text="PLAY", command=MediaControl.Play)
Button2 = tk.Button(music_player, width=5, height=3, text="STOP", command=MediaControl.Stop)
Button3 = tk.Button(music_player, width=5, height=3, text="PAUSE", command=MediaControl.Pause)
Button4 = tk.Button(music_player, width=5, height=3, text="UNPAUSE", command=MediaControl.Unpause)

var = tk.StringVar()
song_title = tk.Label(music_player, textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")

music_player.mainloop()