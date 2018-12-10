##################################################################
#                           BY MINZORD                           #
##################################################################

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image, ImageTk
import sys
import os


def craftdestiny():
    os.system("echo  '' >> /etc/pacman.conf")
    os.system("echo  '[craftdestiny]' >> /etc/pacman.conf")
    os.system("echo  'SigLevel = Never' >> /etc/pacman.conf")
    os.system("echo  'Server = https://miroir.craftdestiny.ml/archlinux-repo/' >> /etc/pacman.conf")
    os.system("sudo pacman -Sy")
    ActivateCraftDestiny.config(state=DISABLED)
    showerror('Fini', "Le dépôt CraftDestiny à bien été ajouté")

def minzord():
    os.system("echo  '' >> /etc/pacman.conf")
    os.system("echo  '[minzord]' >> /etc/pacman.conf")
    os.system("echo  'SigLevel = Never' >> /etc/pacman.conf")
    os.system("echo  'Server = https://minzordos.000webhostapp.com/Repo/' >> /etc/pacman.conf")
    os.system("sudo pacman -Sy")    
    ActivateMinzord.config(state=DISABLED)
    showerror('Fini', "Le dépot Minzord à bien été ajouté")

windows = Tk()

########################################################
#                  CREATTON DE LA FENETRE +            #
#                          TITLE                       #
########################################################

windows.title('Actualia - Repository Manager') #Nom de programme
windows.geometry('620x400') #Taille de la fenetre
windows.resizable(width=False, height=False) #empêcher de redimensionner le programme

canvas = Canvas(windows, width=457, height=90)
canvas.pack()

photo = Image.open("/usr/bin/actualia/logo.png")

photo.thumbnail((457, 120), Image.BICUBIC)

logo = ImageTk.PhotoImage(photo)
canvas.create_image(0, 0, image=logo, anchor=NW)

labelfont = ('times', 14, 'bold')

widget1 = Label(windows, text="\nDépôt CraftDestiny")
widget2 = Label(windows, text="Dépôt Minzord")

ActivateCraftDestiny = Button(windows, text='ACTIVER', height=2, width=30, command=craftdestiny)
ActivateCraftDestiny.pack()
ActivateCraftDestiny.place(x=170, y=133)

ActivateMinzord = Button(windows, text='ACTIVER', height=2, width=30, command=minzord)
ActivateMinzord.pack()
ActivateMinzord.place(x=170, y=237)

widget1.config(font=labelfont)
widget1.config(fg='green')
widget1.pack()

widget2.config(font=labelfont)
widget2.config(fg='green')
widget2.pack(pady=75)

messagebox.showerror("'Bonjour', "Hello, everybody les enfants, salut c'est Sébastien on Youtube et 3w.actualia.fr. \nJe ne cesserai de vous le répéter sans m'en lasser et vous le savez.")



windows.mainloop()
