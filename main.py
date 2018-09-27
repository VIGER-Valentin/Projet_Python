#imports
import sys
import logging
import begin
import time
import os
import parcours
import comparator 

@begin.start
@begin.convert(refresh=int, depth=int) 
def run(folderPath, logFile, refresh=15, depth=5): #nos arguments pour la ligne de commande
    oldList = None
    newList = None    
    if(depth <= 0):
        logging.error("Error, depth is negative or null") #si l'utilisateur rentre une valeur négtive ou nulle
        return
    if(refresh <= 0):
        logging.error("Error, refresh is negative or null")
        return
    if(os.path.isdir(folderPath) == True): #vérification des chemin et fichier donnés
        if(os.path.exists(logFile) == True):
            while(True):
                print(time.strftime("%H:%M:%S")+" - Checking Folder")
                if(oldList == None):
                    temp = parcours.parcoursBase(folderPath) #parcours du fichier
                    oldList = parcours.parcours(temp,depth)
                else:
                    temp = parcours.parcoursBase(folderPath) #pareil qu'au dessus 
                    newList = parcours.parcours(temp,depth)
                    comparator.recur(newList,oldList,logFile)
                    oldList = newList
                    newList = None
                time.sleep(refresh)
        else:
            logging.error(" Log file can not be found")  #si les chemins ne sont pas bons
    else:
        logging.error(" Folder path is wrong")
    
    

    
