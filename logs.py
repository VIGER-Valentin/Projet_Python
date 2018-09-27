import logging
import time
import sys

def newFileLog(logFile, file):
    logging.basicConfig(filename=logFile,level=logging.INFO)
    logging.info(time.strftime("%d-%b-%y %H:%M:%S")+"  new file "+file+" created")
    return

def newFolderLog(logFile, folder):
    logging.basicConfig(filename=logFile,level=logging.INFO)
    logging.info(time.strftime("%d-%b-%y %H:%M:%S")+"  new folder "+folder+" created")
    return

def supprFileLog(logFile, file):
    logging.basicConfig(filename=logFile,level=logging.INFO)
    logging.info(time.strftime("%d-%b-%y %H:%M:%S")+"  file "+file+" deleted")
    return

def supprFolderLog(logFile, folder):
    logging.basicConfig(filename=logFile,level=logging.INFO)
    logging.info(time.strftime("%d-%b-%y %H:%M:%S")+"  folder "+folder+" deleted")
    return
    
def modifFileLog(logFile, file, modifTime):
    logging.basicConfig(filename=logFile,level=logging.INFO)
    logging.info(time.strftime("%d-%b-%y %H:%M:%S")+"  file "+file+" modified at "+modifTime)
    return  
    
def modifFolderLog(logFile, folder, modifTime):
    logging.basicConfig(filename=logFile,level=logging.INFO)
    logging.info(time.strftime("%d-%b-%y %H:%M:%S")+"  folder "+folder+" modified at "+modifTime)
    return  
