# Bibliotekų ir modulių inportavimas
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk


# Pakeidžiame tkinter grafinio interfeiso sukūrimui
root = Tk()

# Grotuvo dydis
root.geometry("516x700+340+10")

# Grotuvo pavadinimas
root.title("MP3 Player")

# Grotuvo fonas
root.config(bg='#0f0f0f')

# Nurodome, kad vartotojai negali keisti grotuvo lango parametrus
root.resizable(False, False)

# Mikser modulio paleidimas
mixer.init()

# Nurodome funkciją muzikinių failų pasirinkimas iš nurodomo aplankalo
def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        print(songs)

        # Nurodome, kad iš pasirinkto aplankalo būtų paleidžiami mp3 ir formato failai
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
        for song in songs:
            if song.endswith(".flac"):
                Playlist.insert(END, song)

# Nustatatome muzikos paleidimo funkciją
def playMusic():
    music_name = Playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# Pridedame sąsajos elementų rėmelį
lower_frm = Frame(root, bg="#000000", width=516, height=200)
lower_frm.place(x=0, y=00)

# Nurodome gif kadrų skaičių
frmcount = 32

# Nurodome gif failo kelią - jis yra tame pačiame aplanke, kuriame yra projekto .py failas.
frms = [PhotoImage(file=os.path.join(os.path.dirname(__file__), 'animation.png')) for i in range(frmcount)]

# Apibrėžiame gif atnaujinimo funkciją
def update(ind):
    frame = frms[ind]
    ind += 1
    if ind == frmcount:
        ind = 0
    lbl.config(image=frame)
    root.after(40, update, ind)

# Nurodome gif vietą sąsajos lange
lbl = Label(root)
lbl.place(x=0, y=0)
root.after(0, update, 0)

# Pridedame meniu su mygtukais
menu_image = Image.open(os.path.join(os.path.dirname(__file__), 'menu.png'))
menu = ImageTk.PhotoImage(menu_image)

# Nurodome dydį
lb_menu = Label(root, image=menu, width=516, height=120)

# Nurodome vietos koordinates
lb_menu.place(x=0, y=580)

# Pridedame mygtukų rėmelį
frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120)
frm_music.place(x=0, y=580)

# Pridedame grojimo mygtuką ir nurodome jo funkciją.
btn_play = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'play.png'))
btn_p = Button(root, image=btn_play, bg='#0f0f0f', height=50, width=50, command=playMusic)
btn_p.place(x=225, y=516)

# Pridedame atkūrimo sustabdymo mygtuką ir nurodome jo funkciją.
btn_stop = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'stop.png'))
btn_s = Button(root, image=btn_stop, bg='#0f0f0f', height=50, width=50, command=mixer.music.stop)
btn_s.place(x=140, y=516)

# Pridedame pauzės mygtuką ir nurodome jo funkciją.
btn_pause = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'pause.png'))
btn_ps = Button(root, image=btn_pause, bg='#0f0f0f', height=50, width=50, command=mixer.music.pause)
btn_ps.place(x=310, y=516)

# Pridedame muzikos aplanko pasirinkimo mygtuką
btn_browse = Button(root, text="Pasirinkti lagaminėlį su muzikos failais", font=('Arial,bold', 15), fg="Black", bg="#FFFFFF", width=48, command=addMusic)
btn_browse.place(x=0, y=572)

# Grojaraščio rodymo pritaikymas
Scroll = Scrollbar(frm_music)
Playlist = Listbox(frm_music, width=100, font=('Arial,bold', 15), bg='#0f0f0f', fg='#00ff00', selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Paleidžiame grotuvo langą
root.mainloop()