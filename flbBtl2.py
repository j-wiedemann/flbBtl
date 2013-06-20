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
#print compteurdelignes

compteur = 0

# nouvelle liste
listepropre = []

while (compteur < compteurdelignes) :
    # tant que le compteur est inférieur au nombre d'element dans la liste
    
    # suppression des espaces et retour a la ligne de l'element en cours
    nouvelleligne = toutesleslignes[compteur].rstrip('\n\r')
    
    # si la ligne en cours est vide
    if nouvelleligne != "":
        # si la ligne en cours n'est pas vide elle est ajoutee a la nouvelle liste
        listepropre.append(nouvelleligne)
    
    # nb boucle = nb element  dans la liste = nb ligne fichier
    compteur = compteur + 1

# affichage de la nouvelle liste
#for ligne in listepropre:
    #print ligne

# nombre de balise [PART]
quantitepart = listepropre.count("[PART]")
print 'nombre de PART :' , quantitepart

# listePART = [ elementsPART , ... ]
listePART =[]

transformations_dict = {"UID":None, 
                                        "OX":None, 
                                        "OY":None, 
                                        "OZ":None, 
                                        "XX":None, 
                                        "XY":None, 
                                        "XZ":None, 
                                        "YX":None, 
                                        "YY":None, 
                                        "YZ":None}
                                        
processkey_dict = {"G":None,            # 1,2 : separating, 3,4 : lying between
                                "KEY":None,         # Key of construction formAlignment
                                "S":None,           # Side of part, reference side
                                "DES":None}         # Designation

# elementsPART = [ "KEY: VALUE"  , ... ]
elementsPART = {"PART":True,
                            "SINGLEMEMBERNUMBER":None,
                            "ASSEMBLYNUMBER":None, 
                            "DESIGNATION":None,
                            "COUNT":None, 
                            "LENGTH":None, 
                            "WIDTH":None, 
                            "HEIGHT":None, 
                            "TRANSFORMATION":transformations_dict, 
                            "PROCESSES":None}
                
# index du premier PART
premierPARTidx =  listepropre.index("[PART]")
# index du PART suivant
deuxiemePARTidx = listepropre.index("[PART]", premierPARTidx+1)
#print 'premier PART idx :',  premierPARTidx
#print 'deuxieme PART idx :',  deuxiemePARTidx
# liste des parametres de ce PART
premierPARTlist = listepropre[premierPARTidx:deuxiemePARTidx]
#print type(premierPARTlist)
#print premierPARTlist[0]
for element in premierPARTlist:
    # pour chaque element de ce PART
    if '[PART]' in element:
        # commence bien par PART ?
        print 'PART ok'
    
    parametresA = element.split(": ")
    elementsPART
    #print parametresA
    if 'SINGLEMEMBERNUMBER' in parametresA:
        #print  'SINGLEMEMBERNUMBER:' , parametresA[1] 
        elementsPART[str(parametresA[0])] = int(parametresA[1])
    if 'COUNT' in parametresA:
        #print  'COUNT:' , parametresA[1] 
        elementsPART[str(parametresA[0])] = int(parametresA[1])
    if 'LENGTH' in parametresA:
        #print  'LENGTH:' , parametresA[1] 
        elementsPART[str(parametresA[0])] = int(parametresA[1])
    if 'HEIGHT' in parametresA:
        #print  'HEIGHT:' , parametresA[1] 
        elementsPART[str(parametresA[0])] = int(parametresA[1])
    if 'WIDTH' in parametresA:
        #print  'WIDTH:' , parametresA[1] 
        elementsPART[str(parametresA[0])] = int(parametresA[1])
    if 'DESIGNATION' in parametresA:
        #print  'DESIGNATION:' , parametresA[1] 
        elementsPART[str(parametresA[0])] = str(parametresA[1])
    if 'TRANSFORMATION' in parametresA:
        # si c'est la clé TRANSFORMATION
        transformations = parametresA[1].split()            # séparations des couples clés/valeurs qui sont dans le deuxieme element de la liste 
        for n in transformations:
            # pour chaque couple 
            transformations = n.split(":")          # séparation clé et valeure
            key = str(transformations[0])           # la clé est le premier element de la lsite et est de type STR
            valeur = transformations[1]         # la valeur est le deuxieme element de la liste
            if "-" in valeur:
                # si il y a le signe NEGATIF
                valeur = valeur[valeur.index("-"):]         # lecture de la valeur a partir du signe
            valeur = int(valeur)            # la valeure est de type INTEGER 
            transformations_dict[key] = valeur          # attribution du couple cle/valeur au dictionnaire
        #print 'transformations:',  transformations
        #print 'transformations_dict', transformations_dict
    if 'PROCESSKEY' in parametresA:
        print parametresA
        split = parametresA[1].split()
        processkey = split[0]
        processkey_label = split[1]
        print "premiersplit",  split
        
        g = processkey[0]
        key = processkey[2:5]
        s = processkey[6]
        des = processkey_label
        #liste = liste.append(premiersplit[0].split("-"))
        liste = [g, key,  s, des]
        print 'PROCESSKEY',  liste
        
print elementsPART        



# Fermeture du fichier
fichier.close()
