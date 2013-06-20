#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ouverture d'un fichier en lecture : r
# notes : ecriture = w ; ajout = a
fichier = open('cutting.btl',"r")

# stockage de chaque ligne dans une liste
# notes : readlines(),readline(),for l in fichier
toutesleslignes = fichier.readlines()

# nombre d'élément dans la liste
compteurdelignes = len(toutesleslignes)
print compteurdelignes

compteur = 0

# nouvelle liste
listepropre = []

while (compteur < compteurdelignes) :
    # tant que le compteur est inférieur au nombre d'element dans la liste
    #print 'le compteur est : ', compteur
    #print 'la ligne est : ', toutesleslignes[compteur].rstrip('\n\r')
    
    # suppression des espaces et retour a la ligne de l'element en cours
    nouvelleligne = toutesleslignes[compteur].rstrip('\n\r')
    
    # si la ligne en cours est vide
    if nouvelleligne != "":
        # si la ligne en cours n'est pas vide elle est ajoutee a la nouvelle liste
        listepropre.append(nouvelleligne)
    
    # nb boucle = nb element 
    compteur = compteur + 1

# affichage de la nouvelle liste
for ligne in listepropre:
    print ligne

# nombre de balise [PART]
quantitepart = listepropre.count("[PART]")
print 'nombre de PART :' , quantitepart


#indexencours = listepropre.index("[PART]")
#print indexencours
compteurPART = 1
#indexdebase = listepropre.index("[PART]")
indexdebase = 0
print 'index de base :', indexdebase
while (compteurPART <= quantitepart) :
    # tant que le compteur de PART est inferieur ou egale a quantitePART
    
    #indexencours = listepropre.index("[PART]")
    indexatrouver = listepropre.index("[PART]", indexdebase, len(listepropre))
    print 'index trouvé :', indexatrouver, 'ligne dans fichier',  indexatrouver +1
    indexdebase = indexatrouver + 1
    #indexsuivant = 
    print 'index de base :', indexdebase
    #listepropre.pop(indexencours)
    for element in listepropre[indexdebase:len(listepropre)]:
        donnees = element.split(",")
        if "LENGTH:" in element :
            print "LONGUEUR :",  donnees[0]
     
    
    compteurPART = compteurPART + 1

# listePART = [ elementsPART , ... ]
listePART =[]
# elementsPART = [ "KEY: VALUE"  , ... ]
elementsPART = {}

# index du premier PART
premierPARTidx =  listepropre.index("[PART]")
# index du PART suivant
deuxiemePARTidx = listepropre.index("[PART]", premierPARTidx+1)
print 'premier PART idx :',  premierPARTidx
print 'deuxieme PART idx :',  deuxiemePARTidx
# liste des parametre de ce PART
premierPARTlist = listepropre[premierPARTidx:deuxiemePARTidx]
print type(premierPARTlist)
print premierPARTlist[0]
for element in premierPARTlist:
    if '[PART]' in element:
        print 'PART ok'
    parametresA = element.split(":")
    print parametresA
    if 'SINGLEMEMBERNUMBER' in parametresA:
       print  'SINGLEMEMBERNUMBER:' , parametresA[1] 
       elementsPART[]
    if 'LENGTH' in parametresA:
        
print premierPARTlist

# Fermeture du fichier
fichier.close()
