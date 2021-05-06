#--Dylan Jean-Baptiste ; Dylan Kessler ; Rouannet Swann--
import os, sys
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import Image, ImageTk
from math import *


# Création de la fenêtre 
fen = tk.Tk()
fen.title("Transformation Image") # On change le nom de la fenêtre.
fen.geometry("1080x720") # On change les dimentions de la fenêtre.
fen.resizable(width=False, height=False) # On empèche de redimentioner la fenêtre.

# -- Transformation : Double Rotation -- #
# Déplacement d'un pixel de l'image sur l'axe des x et des y simultanément.

# Revient à décaler l'image d'un pixel vers le coin inférieur droit.

# Le coin inférieur droit est recopié au coin supérieur gauche. Pas de contrainte de taille d'image. Période: ppcm(largeur,hauteur).

def doublerotation(rotat):          # Le nombre de rotation correspond au nombre de ligne ou de colonne soit : ppcm(largeur,hauteur).
    global dup,ligne,colonne,tableaupix,tableaupix2,dup2,img
    for a in range(rotat):          # Permet de trouver la periode.
        for j in range(colonne):        # parcourir la colonne
            for i in range(ligne):      #parcourir la ligne
                tableaupix2[i,j]=(255, 255, 255)    # On transforme l'image en un rectangle blanc.
        for j in range(colonne):                    # parcourir la colonne
            for i in range(ligne):                  #parcourir la ligne
                if i+1 == ligne and j+1 < colonne:      # On traite la derniere ligne de l'image sauf la derniere case.
                    tableaupix2[0,j+1]=tableaupix[i,j]
                if j+1 == colonne and i+1 < ligne:          # On traite la derniere colonne sauf la derniere case.
                    tableaupix2[i+1,0]=tableaupix[i,j]
                if i+1 == ligne and j+1 == colonne:         # On traite la derniere case.
                    tableaupix2[0,0]=tableaupix[i,j]
                if i+1 < ligne and j+1 < colonne:           # On traite toutes les autres case.
                    tableaupix2[i+1,j+1]=tableaupix[i,j]
        for j in range(colonne):
            for i in range(ligne):
                tableaupix[i,j]=tableaupix2[i,j]            # On copie le tableau de pixels dans celui de depart.
                                                  # affiche le résultat finale .
    dup2 = ImageTk.PhotoImage(dup) # On affiche l'image dans la fenêtre
    lab.configure(image=dup2)
    lab.image=dup2


# -- Transformation : Rotation en X  -- #
# Pour chaque pixel, si son numéro de ligne est pair, on l'augmente de 2, s'il est impair on le diminue de 2.
# Même chose pour la colonne. Contrainte de taille d'image : hauteur et largeur paires. Période : ppcm(larg/2, haut/2).
# Il faut effectuer un total de 32 transformations d'affilé pour revenir à l'image originale pour une image de 64x64 par exemple.

def rotX(rotat):            #  Le nombre de rotation correspond a ppcm(ligne//2,colonne//2), l'image doit avoir un nombre de ligne et de colonne pair.
    global dup,ligne,colonne,tableaupix,tableaupix2,dup2,img
    for a in range(rotat):      # Permet de trouver la periode.
        for j in range(colonne):     # parcourir la colonne.
            for i in range(ligne):      #parcourir la ligne.
                tableaupix2[i,j]=(255, 255, 255)    # On transforme l'image en un rectangle blanc.
        for j in range(colonne):        # parcourir la colonne.
            for i in range(ligne):       #parcourir la ligne.
                if i%2 == 0:
                    if j%2 ==0:
                        tableaupix2[(i+2)%ligne,(j+2)%colonne]=tableaupix[i,j]      # On utilise modulo pour eviter les pixels qui sortent de la matrice, colonne pair et ligne pair donc on augmente chacun de 2.
                    else:
                        tableaupix2[(i+2)%ligne,(j-2)%colonne]=tableaupix[i,j]      # Ligne pair mais colonne inpair, on augmente donc de 2 la ligne et on diminue de 2 la colonne.
                else:
                    if j%2==0:
                        tableaupix2[(i-2)%ligne,(j+2)%colonne]=tableaupix[i,j]      # Ligne inpair mais colonne pair , on diminue de 2 la ligne et on augmente de 2 la colonne.
                    else:
                        tableaupix2[(i-2)%ligne,(j-2)%colonne]=tableaupix[i,j]      # Ligne et colonne inpair donc on diminue les 2 .
        for j in range(colonne):
            for i in range(ligne):
                tableaupix[i,j]=tableaupix2[i,j]    # On copie le tableau de pixels dans celui de depart.
    dup2 = ImageTk.PhotoImage(dup) # On affiche l'image dans la fenêtre
    lab.configure(image=dup2)
    lab.image=dup2 # affiche le résultat finale .

# -- Variable
imgpath = "" # Cette variable prendra plus tard le chemin d'accès de l'image.

# -- Fonctions
def openfile(): # La fonction openfile permet d'ouvrir l'explorateur de fichier et de pouvoir choisir l'image que l'on souhaite traiter.
    global imgpath,dup,img,ligne,colonne,tableaupix,tableaupix2,dup2
    imgpath = filedialog.askopenfilename(initialdir = "/Images",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*"))) # On ouvre l'explorateur de fichier windows
    img = Image.open(imgpath) # Une fois l'image choisis, on ouvre son chemin d'accès dans img
    img.thumbnail((256,256)) # On redimentionne l'image à 256px par 256px
    img2 = ImageTk.PhotoImage(img) # On affiche l'image dans la fenêtre
    lab.configure(image=img2)
    lab.image=img2
    img = Image.open(imgpath)
    img.thumbnail((256,256))

# On crée une copie de l'image.
    dup = Image.open(imgpath)
    dup.thumbnail((256,256))

# On récupère les informations de dimentions de l'image.
    ligne, colonne = img.size

# On charge les deux images dans une matrice de pixels réspective.
    tableaupix=img.load() # Image originale
    tableaupix2=dup.load() # Copie de l'image

def recuptext(): # Fonction pour recuperer les informations necessaire pour le bouton valider
    global nombreTransfo,dup,img,ligne,colonne,tableaupix,tableaupix2,dup2
    content = nombreTransfo.get()   #Recupere le nombre de transformation choisi
    transfochoisi = v.get()     #Recupere la transformation choisi
    if transfochoisi == 'Double rotation': # Si double rotation est choisi
        showwarning('Attention',' Pour revenir a l image initial la periode  doit correspondre a n*ppcm(largeur,hauteur)') #Ligne d'alerte pour double rotation
        doublerotation(int(content))    #Execution de la fonction double rotation
    elif transfochoisi == 'Rotation en X': # Si rotation en x est choisi
        showwarning('Attention','Pour revenir a l image initial la periode  doit correspondre a n*ppcm(largeur/2,hauteur/2)') # Ligne d'alerte pour la fonction rotX
        rotX(int(content)) #Exécution de la fonction rotX

def recuptext2(): # Fonction pour recuperer les informations necessaire pour le bouton pas
    global nombreTransfo,dup,img,ligne,colonne,tableaupix,tableaupix2,dup2
    content = nombreTransfo.get() #Recupere le nombre de transformation choisi
    transfochoisi = v.get() #Recupere la transformation chois
    compteur = 1
    ppcm = (ligne * colonne)/gcd(ligne,colonne) #Calcul du ppcm pour double rotation
    ppcm2 = (ligne//2 * colonne//2)/gcd(ligne//2,colonne//2) #Calcul du ppcm pour rotX

    if transfochoisi == 'Double rotation':  # Si double rotation est choisi
        showwarning('Attention','Si vous voulez arreter, mettez le nombre de transformations a 0 et reappuyer sur PAS') #Ligne d'alerte pour double rotation
        while(compteur<int(ppcm)):
            doublerotation(int(content))        #Execution de la fonction double rotation
            fen.update()                        #Rafraichissement de la page
            compteur = compteur + int(content)      # compteur pour faire le pas
    elif transfochoisi == 'Rotation en X':      # Si rotation en x est choisi
        showwarning('Attention','Si vous voulez arreter, mettez le nombre de transformations a 0 et reappuyer sur PAS; plus la taille de limage est grande plus vous devrez prendre un grands nombre de transformation') # Ligne d'alerte pour la fonction rotX
        while(compteur<int(ppcm)):
            rotX(int(content))#Exécution de la fonction rotX
            fen.update()#Rafraichissement de la page
            compteur = compteur + int(content)# compteur pour faire le pas

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

BoutonValider = tk.Button(fen, text ="Valider", command = recuptext) #Bouton Valider
BoutonValider.pack()

BoutonValider2 = tk.Button(fen, text ="Pas", command = recuptext2) #Bouton pas
BoutonValider2.pack()

BoutonQuitter = tk.Button(fen, text = "Fermer", command = fen.destroy) #Bouton Fermer
BoutonQuitter.pack(side = tk.RIGHT, padx = 0, pady = 0)

BoutonOuvrir = tk.Button(fen, text = "Ouvrir", command = openfile) #Bouton Ouvrir
BoutonOuvrir.pack(side = tk.LEFT, padx = 0, pady = 0)


# Label
lab = tk.Label(fen)
lab.pack(pady = 150) #Placement de l'image



# Boucle principale
fen.mainloop()
