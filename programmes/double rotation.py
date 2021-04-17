import os, sys
from PIL import Image
img = Image.open('47a.jpg')

dup = Image.open('47a.jpg')

ligne, colonne = img.size

print(colonne)
print(ligne)


tableaupix=img.load()#charger l'image dans une matrice de pixels
tableaupix2=dup.load()

for j in range(colonne):
    for i in range(ligne):
        tableaupix2[i,j]=(255, 255, 255)
dup.show()


def fnc(rotat):
    for a in range(rotat):
        for j in range(colonne):
            for i in range(ligne):
                tableaupix2[i,j]=(255, 255, 255)
        for j in range(colonne):
            for i in range(ligne):
                if i+1 >= ligne and j+1 < colonne:
                    tableaupix2[0,j+1]=tableaupix[i,j]
                if j+1 >= colonne and i+1 < ligne:
                    tableaupix2[i+1,0]=tableaupix[i,j]
                if i+1 >= ligne and j+1 >= colonne:
                    tableaupix2[0,0]=tableaupix[i,j]
                if i+1 < ligne and j+1 < colonne:
                    tableaupix2[i+1,j+1]=tableaupix[i,j]
        dup.show()
        for j in range(colonne):
            for i in range(ligne):
                tableaupix[i,j]=tableaupix2[i,j]


fnc(10)