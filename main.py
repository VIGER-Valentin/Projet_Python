import sys
import logging
import begin
import time
import os

@begin.start
@begin.convert(refresh=int, depth=int)
def run(folder, logFile, refresh=15, depth=5):
    if(os.path.isdir(folder) == True):
        if(os.path.exists(logFile) == True):
            while(True):
                #TO DO : function parcours
                print(time.strftime("%H:%M:%S")+" - Checking Folder")
                time.sleep(refresh)
        else:
            logging.error(" Log file can not be found")  
    else:
        logging.error(" Folder path is wrong")
    
    
