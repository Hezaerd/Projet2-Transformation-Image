# -- Swann ROUANET -- #


# Les modules qu'on utilise sont : tkinter, tkinter filedialog, tkinter messagebox et PIL.
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import Image, ImageTk


# Création de la fenêtre
fen = tk.Tk()
fen.title("Transformation Image") # On change le nom de la fenêtre.
fen.geometry("1080x720") # On change les dimentions de la fenêtre.
fen.resizable(width=False, height=False) # On empèche de redimentioner la fenêtre.


# -- Variable
imgpath = "" # Cette variable prendra plus tard le chemin d'accès de l'image.


# -- Fonctions
def openfile(): # La fonction openfile permet d'ouvrir l'explorateur de fichier et de pouvoir choisir l'image que l'on souhaite traiter.
    global imgpath
    imgpath = filedialog.askopenfilename(initialdir = "/Images",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*"))) # On ouvre l'explorateur de fichier windows
    img = Image.open(imgpath) # Une fois l'image choisis, on ouvre son chemin d'accès dans img
    img.thumbnail((256,256)) # On redimentionne l'image à 256px par 256px
    img = ImageTk.PhotoImage(img) # On affiche l'image dans la fenêtre
    lab.configure(image=img)
    lab.image=img

def recuptext():
    global nombreTransfo
    content = nombreTransfo.get()
    print(content)


# -- Interface Homme Machine
# Menu déroulant 1 - Choix de la transformation
listeOptions = ('Double rotation', 'Rotation en X') # On défini la liste des transfomations possible
v = tk.StringVar() 
v.set(listeOptions[0])
om = tk.OptionMenu(fen, v, *listeOptions)
om.pack(side = tk.TOP, padx = 0, pady = 0)

nombreTransfo = tk.StringVar()
e = tk.Entry(fen, textvariable=nombreTransfo)
e.pack()

BoutonValider = tk.Button(fen, text ="Valider", command = recuptext)
BoutonValider.pack()

BoutonQuitter = tk.Button(fen, text = "Fermer", command = fen.destroy)
BoutonQuitter.pack(side = tk.RIGHT, padx = 0, pady = 0)

BoutonOuvrir = tk.Button(fen, text = "Ouvrir", command = openfile)
BoutonOuvrir.pack(side = tk.LEFT, padx = 0, pady = 0)


# Label
lab = tk.Label(fen)
lab.pack(side = tk.LEFT)

# Boucle principale
fen.mainloop()
