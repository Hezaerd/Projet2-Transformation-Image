import os, sys # importer
from PIL import Image
img = Image.open('47a.jpg')

dup = Image.open('47a.jpg')

ligne, colonne = img.size

print(colonne)
print(ligne)


tableaupix=img.load()#charger l'image dans une matrice de pixels
tableaupix2=dup.load()




def doublerotation(rotat): # le nombre de rotation correspond au nombre  de ligne ou de colonne  ppcm(largeur,hauteur)
    for a in range(rotat):# permet de trouver la periode
        for j in range(colonne):
            for i in range(ligne):
                tableaupix2[i,j]=(255, 255, 255)# je met mon image a blanc
        for j in range(colonne):
            for i in range(ligne):
                if i+1 == ligne and j+1 < colonne:# traitement de la derniere ligne de  l'image sauf la derniere case
                    tableaupix2[0,j+1]=tableaupix[i,j]
                if j+1 == colonne and i+1 < ligne: # traitement de la derniere colonne sof la derniere case
                    tableaupix2[i+1,0]=tableaupix[i,j]
                if i+1 == ligne and j+1 == colonne:# Traitement de la derniere case
                    tableaupix2[0,0]=tableaupix[i,j]
                if i+1 < ligne and j+1 < colonne:# traitement de toute les autres case
                    tableaupix2[i+1,j+1]=tableaupix[i,j]
        for j in range(colonne):
            for i in range(ligne):
                tableaupix[i,j]=tableaupix2[i,j]# copie le tableau de pixels dans celui de depart
        if a%20==0:# affiche une image toute les 20 rotation
            dup.show()
    dup.show()# affiche l'image obtenue

#Pour chaque pixel, si son numéro de ligne est pair, on l'augmente de 2, s'il est impair on le diminue de 2.
#Même chose pour la colonne. Contrainte de taille d'image : hauteur et largeur paires. Période : ppcm(larg/2, haut/2)
def rotX(rotat):# ppcm(ligne//2,colonne//2), l'image doit avoir un nombre de ligne et de colonne pair
    for a in range(rotat):
        for j in range(colonne):
            for i in range(ligne):
                tableaupix2[i,j]=(255, 255, 255)#je met mon image a blanc
        for j in range(colonne):
            for i in range(ligne):
                if i%2 == 0:
                    if j%2 ==0:
                        tableaupix2[(i+2)%ligne,(j+2)%colonne]=tableaupix[i,j]# on le place a i+2%ligne et j+2%colonne ,ce qui permet de rester dans l'encadrement
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

rotX(32)