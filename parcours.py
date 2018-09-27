import os
import platform
import time

#Fonction de parcours d'arborescence d'un chemin précis
#Paramètres :
#   _ rootPath : chemin initial du parcours
#   _ nbLvl : nombre de niveau max à parcourir dans l'arborescence
def parcoursBase(rootPath) :
    arborescence = []

    for path, dirs, files in os.walk(rootPath) :
        for folder in dirs :
            if (platform.system() == 'Windows') :
                arborescence.append(([rootPath+"\\"+folder],time.ctime(os.path.getmtime(rootPath+"\\"+folder))))
            elif (platform.system() == 'Linux') :
                arborescence.append(([rootPath+"/"+folder],time.ctime(os.path.getmtime(rootPath+"/"+folder))))
        for file in files :
            if (platform.system() == 'Windows') :
                arborescence.append((rootPath+"\\"+file,time.ctime(os.path.getmtime(rootPath+"\\"+file))))
            elif (platform.system() == 'Linux') :
                arborescence.append((rootPath+"/"+file,time.ctime(os.path.getmtime(rootPath+"/"+file))))
        break

    return arborescence

#Fonction de parcours général (Wrapper)
def parcours(arborescence,nbLvl) :
    if (len(arborescence) > 0) :
        i = 0
        for element in arborescence :
            if ((isinstance(element[0],list)) and (nbLvl > 0)):
                tempo = parcoursBase(arborescence[i][0][0])
                if (len(tempo) > 0):
                    tempo = parcours(tempo,nbLvl-1)
                    arborescence[i][0].append(tempo)
                    i += 1
            else :
                break
            
    return arborescence
