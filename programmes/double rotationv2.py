# -- Dylan Jean-Baptiste & Dylan Kesler & Swann Rouanet & Jeanne-Louise Lucas & Charlesia Dan -- #

# Les librairies qu'on utilise sont : os, system et PIL
import os, sys
from PIL import Image


# On ouvre l'image.
img = Image.open('47a.jpg')

# On crée une copie de l'image.
dup = img

# On récupère les informations de dimentions de l'image.
ligne, colonne = img.size

# On charge les deux images dans une matrice de pixels réspective.
tableaupix=img.load() # Image originale
tableaupix2=dup.load() # Copie de l'image


# -- Transformation : Double Rotation -- #
# A MODIFIER ! : QUE FAIT LA TRANSFORMATION !!! #
def doublerotation(rotat): # Le nombre de rotation correspond au nombre de ligne ou de colonne soit : ppcm(largeur,hauteur).
    for a in range(rotat): # Permet de trouver la periode.
        for j in range(colonne):
            for i in range(ligne):
                tableaupix2[i,j]=(255, 255, 255) # On transforme l'image en un rectangle blanc.
        for j in range(colonne):
            for i in range(ligne):
                if i+1 == ligne and j+1 < colonne: # On traite la derniere ligne de l'image sauf la derniere case.
                    tableaupix2[0,j+1]=tableaupix[i,j]
                if j+1 == colonne and i+1 < ligne: # On traite la derniere colonne sauf la derniere case.
                    tableaupix2[i+1,0]=tableaupix[i,j]
                if i+1 == ligne and j+1 == colonne: # On traite la derniere case.
                    tableaupix2[0,0]=tableaupix[i,j]
                if i+1 < ligne and j+1 < colonne: # On traite toutes les autres case.
                    tableaupix2[i+1,j+1]=tableaupix[i,j]
        for j in range(colonne):
            for i in range(ligne):
                tableaupix[i,j]=tableaupix2[i,j] # On copie le tableau de pixels dans celui de depart.
    dup.show() # affiche le résultat finale 

    
# -- Transformation : Rotation en X  -- #
# Pour chaque pixel, si son numéro de ligne est pair, on l'augmente de 2, s'il est impair on le diminue de 2.
# Même chose pour la colonne. Contrainte de taille d'image : hauteur et largeur paires. Période : ppcm(larg/2, haut/2)
# Il faut effectuer un total de 32 transformations d'affilé pour revenir à l'image originale.
def rotX(rotat):# ppcm(ligne//2,colonne//2), l'image doit avoir un nombre de ligne et de colonne pair
    for a in range(rotat):
        for j in range(colonne):
            for i in range(ligne):
                tableaupix2[i,j]=(255, 255, 255) # On transforme l'image en un rectangle blanc.
        for j in range(colonne):
            for i in range(ligne):
                if i%2 == 0:
                    if j%2 ==0:
                        tableaupix2[(i+2)%ligne,(j+2)%colonne]=tableaupix[i,j] # On le place a i+2%ligne et j+2%colonne ,ce qui permet de rester dans l'encadrement
                    else:
                        tableaupix2[(i+2)%ligne,(j-2)%colonne]=tableaupix[i,j]
                else:
                    if j%2==0:
                        tableaupix2[(i-2)%ligne,(j+2)%colonne]=tableaupix[i,j]
                    else:
                        tableaupix2[(i-2)%ligne,(j-2)%colonne]=tableaupix[i,j]
        for j in range(colonne):
            for i in range(ligne):
                tableaupix[i,j]=tableaupix2[i,j]
        if a%5==0:
            dup.show()
    dup.show()
