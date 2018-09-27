import os
import platform
import time

#Fonction de parcours d'arborescence d'un chemin précis
#Paramètres :
#   _ rootPath : chemin initial du parcours
#   _ nbLvl : nombre de niveau max à parcourir dans l'arborescence
def parcoursBase(rootPath) :
    arborescence = []           #Arborescence retournée sous forme de liste

    #Identification du contenu visible directement à la racine
    for path, dirs, files in os.walk(rootPath) :
        #Récupération des dossiers
        for folder in dirs :
            #Vérification de l'OS utilisé (Windows ou Linux)
            #Ajout du résultat dans l'arborescence sous forme de tuple : (liste,string)
            #([Chemin du dossier],date de dernière modification)
            if (platform.system() == 'Windows') :
                arborescence.append(([rootPath+"\\"+folder],time.ctime(os.path.getmtime(rootPath+"\\"+folder))))
            elif (platform.system() == 'Linux') :
                arborescence.append(([rootPath+"/"+folder],time.ctime(os.path.getmtime(rootPath+"/"+folder))))
        #Récupération des fichiers
        for file in files :
            #Vérification de l'OS utilisé (Windows ou Linux)
            #Ajout du résultat dans l'arborescence sous forme de tuple : (string,string)
            #(Chemin du fichier,date de dernière modification)
            if (platform.system() == 'Windows') :
                arborescence.append((rootPath+"\\"+file,time.ctime(os.path.getmtime(rootPath+"\\"+file))))
            elif (platform.system() == 'Linux') :
                arborescence.append((rootPath+"/"+file,time.ctime(os.path.getmtime(rootPath+"/"+file))))
        break

    return arborescence

#Fonction de parcours général (Wrapper)
def parcours(arborescence,nbLvl) :
    #Vérification que l'arborescence n'est pas vide
    if (len(arborescence) > 0) :
        i = 0
        #Parcours en profondeur de chaque dossier via un appel récurrent de la fonction "parcours"
        for element in arborescence :
            #Vérification que l'élément courant est bien une liste et donc un dossier et non pas une string donc un fichier
            if ((isinstance(element[0],list)) and (nbLvl > 0)):
                tempo = parcoursBase(arborescence[i][0][0])
                if (len(tempo) > 0):
                    tempo = parcours(tempo,nbLvl-1)
                    arborescence[i][0].append(tempo)
                    i += 1
            else :
                break
            
    return arborescence
