from tkinter import ACTIVE, END, NW, SINGLE, W, Button, Frame, Label, Listbox, Scale, Scrollbar, StringVar, ttk, Tk
from PIL import ImageTk, Image
import os
from pygame import mixer
import time
from pydub import AudioSegment
from mutagen.mp3 import MP3

c1 = "#ffffff"
c2 = "#ffffff"
c3 = "#333333"
c4 = "#CFC7F8"

window = Tk()
window.title ("meow")
window.geometry('400x310')
window.configure(background=c1)
window.resizable(width=False, height=False)

#fun
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def next_music():
    playing = running_song['text']
    index = song.index(playing)
    new = index + 1
    playing = song[new]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show_music()

    listbox.select_set(new)
    running_song['text'] = playing


def previous_music():
    playing = running_song['text']
    index = song.index(playing)
    new = index - 1
    playing = song[new]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show_music()

    listbox.select_set(new)
    running_song['text'] = playing

def volume_music(x):
    volume = int(x)/100
    mixer.music.set_volume(volume)

def speedcontrol(x):
    speed = int(x)*1

def slidebar_music(x):
    sliderlabel.config(text=int(sliderbar.get()))

def play_time():
    current_time = mixer.music.get_pos() / 1000
    convert1 = time.strftime('%M:%S', time.gmtime(current_time))
    #global 
    current_song = show_music().curselection()
    song1 = show_music().get(current_song)
    song1 = f'C:/Users/Aimpr/OneDrive/Desktop/music/song/{song1}.mp3'
    song_m = MP3(song)
    song_l = song_m.info.length
    convert_songL = time.strftime('%M:%S', time.gmtime(song_l))

    running_time.config(text = f'Time: {convert1} of {convert_songL}')
    running_time.after(1000, play_time)



#frame
left_frame = Frame(window, width=150, height=150, bg=c1)
left_frame.grid(row=0, column=1, padx=0)

right_frame = Frame(window, width=250, height=150, bg=c3)
right_frame.grid(row=0, column=2, padx=0)

down_frame = Frame(window, width=400, height=200, bg=c4)
down_frame.grid(row=1, columnspan=3, column=0, padx=0 ,pady=1)

#musiclist
listbox = Listbox(right_frame, selectmode=SINGLE, font=("Arial 9 bold"), width=30, bg=c3, fg=c1)
listbox.grid(row=0, column=0)

#list_num = [1, 2, 3, 4, 5]
#for i in list_num:
    #listbox.insert(END, i)

sb = Scrollbar(right_frame)
sb.grid(row=0, column=1)

listbox.config(yscrollcommand=sb.set)
sb.config(command=listbox.yview)

#image icon
im_1 = Image.open('icon/1.png')
im_1 = im_1.resize((40,40))
im_1 = ImageTk.PhotoImage(im_1)
next_button = Button(down_frame, height=60, image=im_1, padx=10, bg=c4, command=next_music)
next_button.place(x=10+250, y=15)


im_2 = Image.open('icon/2.png')
im_2 = im_2.resize((40,40))
im_2 = ImageTk.PhotoImage(im_2)
stop_button = Button(down_frame, height=60, image=im_2, padx=10, bg=c4, command=pause_music)
stop_button.place(x=10+295, y=15)


im_3 = Image.open('icon/3.png')
im_3 = im_3.resize((70,70))
im_3 = ImageTk.PhotoImage(im_3)
app_im = Label(left_frame, height=130, image=im_3, padx=10, bg=c1)
app_im.place(x=35, y=15)

im_4 = Image.open('icon/4.png')
im_4 = im_4.resize((40,40))
im_4 = ImageTk.PhotoImage(im_4)
play_button = Button(down_frame, height=60, image=im_4, padx=10, bg=c4, command=play_music)
play_button.place(x=10+205, y=15)

im_5 = Image.open('icon/5.png')
im_5 = im_5.resize((40,40))
im_5 = ImageTk.PhotoImage(im_5)
previous_button = Button(down_frame, height=60, image=im_5, padx=10, bg=c4, command=previous_music)
previous_button.place(x=10+160, y=15)

im_6 = Image.open('icon/6.png')
im_6 = im_6.resize((40,40))
im_6 = ImageTk.PhotoImage(im_6)
re_button = Button(down_frame, height=60, image=im_6, padx=10, bg=c4, command=unpause_music)
re_button.place(x=10+340, y=15)

volumbar = Scale(down_frame, from_=100, to=0, bg=c4, orient='horizontal', length= 120, command=volume_music)
volumbar.set(50)
volumbar.place(x=10+10, y=25)

sliderbar = ttk.Scale(down_frame, from_=0, to=100, orient='horizontal', value=0, length= 220, command=slidebar_music)
sliderbar.place(x=10+160, y=85)


sliderlabel = Label(down_frame, text="0")
sliderlabel.place(x=10+200, y=115)

speedcon = Scale(down_frame, from_=2, to=0, bg=c4, orient='horizontal', length= 120, command=speedcontrol)
speedcon.set(1)
speedcon.place(x=10+10, y=80)

#slider = Label()
#slider.pack(pady=10)

#line = Label(left_frame, width=200, height=1, padx=10)
#line.place(x=0, y=1)

running_time = Label(down_frame, text = "Time of song", font=("Ivy 10"), width=200, height=1, padx=10, bg=c4, fg = c3, anchor=NW)
running_time.place(x=230, y=115 )

running_song = Label(down_frame, text = "Choose a Song", font=("Ivy 10"), width=200, height=1, padx=10, bg=c1, fg = c3, anchor=NW)
running_song.place(x=0, y=1 )


os.chdir(r'C:\Users\Aimpr\OneDrive\Desktop\music\song')
song = os.listdir()


def show_music():
    for i in song:
        listbox.insert(END, i)

show_music()
mixer.init()
music_state = StringVar()
music_state.set("meow")
window.mainloop()
