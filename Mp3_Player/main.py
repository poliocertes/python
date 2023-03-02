# Mp3_Player by Jacek

import os
import time
import sys
import tkinter
from tkinter import *
from tkinter import filedialog, ttk

import pygame
from mutagen.mp3 import MP3
from pygame import event, MOUSEBUTTONDOWN

pygame.init()
player = Tk()
player.title('MiMoZu Player')
player.iconbitmap('player.ico')
player.geometry('600x400')
COLOR = "#0066CC"
COLOR_2 = "#3399FF"
player.resizable(False, False)
player.configure(bg=COLOR)

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.mixer.init()
repeat = 0
paused = FALSE
muted = FALSE
global currentSong


# play time function
def play_time():
    global current_time
    current_time = pygame.mixer.music.get_pos() / 1000
    song = Playlist.get(ACTIVE)
    song_mut = MP3(song)
    global song_lenght
    song_lenght = song_mut.info.length
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_lenght))
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
    song_slider.config(value=current_time)
    current_time += 1
    song_slider.after(125, play_time)
    song_time_label.config(text="Song Time: " + str(converted_current_time) + " / " + str(converted_song_length))


# stop playing function
def stop():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    Playlist.selection_clear(ACTIVE)
    button1.config(borderwidth=0)


# current song name function
def current_song_name():
    current_song = Playlist.get(ACTIVE)
    button1.config(borderwidth=1)
    song_slider_label.config(text="Now playing: " + current_song)


# play function
def play():
    song_list_not_empty = Playlist.get(0, END)
    if song_list_not_empty:
        if not paused:

            SONG_END = pygame.USEREVENT + 1
            pygame.mixer.music.set_endevent(SONG_END)
            pygame.mixer.music.load(Playlist.get(ACTIVE))
            current_song_name()
            pygame.mixer.music.play(repeat)
            play_time()
            slider_position = int(song_lenght)
            song_slider.config(to=slider_position, value=0)
            while True:
                for event in pygame.event.get():
                    if event.type == SONG_END:
                        next_song()
                player.update()
        else:
            pygame.mixer.music.unpause()
            button1.config(borderwidth=1)
            button3.config(borderwidth=0)
    else:
        tkinter.messagebox.showerror(title="Error", message="No songs on the playlist")


# pause function
def pause():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = TRUE
        button1.config(borderwidth=0)
        button3.config(borderwidth=1)
    else:
        pygame.mixer.music.unpause()
        paused = FALSE
        button3.config(borderwidth=0)


# next song
def next_song():
    song_list_not_empty = Playlist.get(0, END)
    if song_list_not_empty:
        try:
            song = Playlist.curselection()
            nextSong = song[0] + 1
            next_song = Playlist.get(nextSong)
            index = Playlist.curselection()[0]
            Playlist.selection_clear(0, END)
            Playlist.selection_set(index + 1)
            Playlist.activate(index + 1)
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()
            current_song_name()
        except:
            nextSong > Playlist.size()
            tkinter.messagebox.showerror(title="Error",
                                         message="That was a last song. No more songs after currrent one.")
            button1.config(borderwidth=0)
    else:
        tkinter.messagebox.showerror(title="Error", message="No songs on the list.")


# previous song
def previous_song():
    song_list_not_empty = Playlist.get(0, END)
    if song_list_not_empty:
        try:
            song = Playlist.curselection()
            previous_song = song[0] - 1
            prev_song = Playlist.get(previous_song)
            index = Playlist.curselection()[0]
            Playlist.selection_clear(0, END)
            Playlist.selection_set(index - 1)
            Playlist.activate(index - 1)
            pygame.mixer.music.load(prev_song)
            pygame.mixer.music.play()
            current_song_name()
        except:
            prev_song < Playlist.get(0)
            tkinter.messagebox.showerror(title="Error",
                                         message="That was a first song. No more songs before currrent one.")
    else:
        tkinter.messagebox.showerror(title="Error", message="No songs on the list.")


# add many songs to the list
def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(END, song)


# add one song to the list
def add_song():
    song = filedialog.askopenfilename(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    Playlist.insert(END, song)


# make music list empty
def del_music():
    pygame.mixer.music.stop()
    Playlist.delete(0, END)
    button1.config(borderwidth=0)


# del one song
def del_one_song():
    pygame.mixer.music.stop()
    Playlist.delete(ANCHOR)


# repeat one song
def repeat_song():
    global repeat
    if repeat >= 0:
        repeat = -1
        button10.config(borderwidth=1, image=repeatPhoto)
    else:
        repeat = 0
        button10.config(borderwidth=0, image=noRepeatPhoto)


# make a list empty
def add_song():
    pygame.mixer.music.stop()
    Playlist.delete(ANCHOR)


# volume adjustment
def volume(X):
    pygame.mixer.music.set_volume(volume_slider.get())


# mute function
def mute():
    global muted
    global last_volume_level
    if muted:
        pygame.mixer.music.set_volume(last_volume_level)
        volume_slider.set(last_volume_level)
        button9.configure(image=soundPhoto, borderwidth=1)
        muted = FALSE
    else:
        last_volume_level = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(0)
        volume_slider.set(0)
        button9.configure(image=mutePhoto, borderwidth=0)
        muted = TRUE


# player exit
def close_player():
    time.sleep(1.0)
    player.destroy()
    time.sleep(1.0)
    quit()


# creating song time progress slider
def slider(X):
    song = Playlist.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(song_slider.get()))


def info():
    tkinter.messagebox.showinfo(title="About", message="MiMoZu Mp3 Player by Jacek")


def mouse_click():
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1: # 1 == left button
            print("click!")


# another stuff
player_menu = Menu(player, tearoff=False)
fileMenu = Menu(player_menu, tearoff=0)
fileMenu.add_command(label="Add folder", command=add_music)
fileMenu.add_command(label="Add song", command=add_song)
fileMenu.add_separator()
fileMenu.add_command(label="Clear playlist", command=del_music)
fileMenu.add_command(label="Delete song from playlist", command=del_one_song)
fileMenu.add_separator()
fileMenu.add_command(label="Turn off player", command=close_player)
player_menu.add_cascade(label="Menu", menu=fileMenu)

aboutMenu = Menu(player_menu, tearoff=0)
aboutMenu.add_command(label="About Player", command=info)
player_menu.add_cascade(label="About", menu=aboutMenu)

style = ttk.Style()
style.configure("TScale", background=COLOR)
volume_slider = ttk.Scale(player, orient=HORIZONTAL, from_=0, to=1, length=125, command=volume, style="TScale")
song_slider = ttk.Scale(player, orient=HORIZONTAL, from_=0, to=100, length=580, command=slider, style="TScale", value=0)
song_slider_label = Label(player, text="Now playing: No songs", background=COLOR, font=("Arial", 12), fg="white")
song_time_label = Label(player, text="Song Time: 0:00", background=COLOR, font=("Arial", 12), fg="white")
volume_slider.set(0.7)
volume_slider.grid(row=2, column=3)

Playlist = Listbox(player, width=85, height=12, font=("Arial", 10), bg=COLOR_2, fg="black",
                   selectbackground="grey", cursor="arrow", bd=0)
playPhoto = PhotoImage(file='start.png')
stopPhoto = PhotoImage(file='stop.png')
pausePhoto = PhotoImage(file='pause.png')
nextPhoto = PhotoImage(file='next.png')
prevPhoto = PhotoImage(file='prev.png')
soundPhoto = PhotoImage(file='sound.png')
mutePhoto = PhotoImage(file='mute.png')
repeatPhoto = PhotoImage(file='repeat.png')
noRepeatPhoto = PhotoImage(file='arrow.png')

button1 = Button(player, image=playPhoto, borderwidth=0, bg=COLOR, command=play)
button2 = Button(player, image=stopPhoto, borderwidth=0, bg=COLOR, command=stop)
button3 = Button(player, image=pausePhoto, borderwidth=0, bg=COLOR, command=pause)
button4 = Button(player, image=prevPhoto, borderwidth=0, bg=COLOR, command=previous_song)
button5 = Button(player, image=nextPhoto, borderwidth=0, bg=COLOR, command=next_song)
button9 = Button(player, image=soundPhoto, borderwidth=0, bg=COLOR, command=mute)
button10 = Button(player, image=noRepeatPhoto, borderwidth=0, bg=COLOR, command=repeat_song)

button1.place(x=5, y=320)
button2.place(x=60, y=320)
button3.place(x=115, y=320)
button4.place(x=170, y=320)
button5.place(x=225, y=320)
button9.place(x=500, y=320)
button10.place(x=550, y=320)

volume_slider.place(x=320, y=323)
song_slider.place(x=10, y=280)
song_time_label.place(x=20, y=215)
song_slider_label.place(x=20, y=245)
player.config(menu=player_menu)
Playlist.pack()
player.configure(bg=COLOR)

player.mainloop()






