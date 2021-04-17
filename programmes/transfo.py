import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import Image, ImageTk

# Création de la fenêtre
fen = tk.Tk()
fen.title("Transformation Image - JeanBaptiste Rouanet & Kessler")
fen.geometry("1080x720")
fen.resizable(width=False, height=False)


# Variable
imgpath = ""

# Fonctions
def openfile():
    global imgpath
    imgpath = filedialog.askopenfilename(initialdir = "/Images",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
    img = Image.open(imgpath)
    img.thumbnail((256,256))
    img = ImageTk.PhotoImage(img)
    lab.configure(image=img)
    lab.image=img

def recuptext():
    global nombreTransfo
    content = nombreTransfo.get()
    print(content)




# Boutons
listeOptions = ('Double rotation', 'Rotation en X')
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
