import logs
def comparator(listeNouvelle : list ,listeAncienne : list,logfile) -> None :
    print("Les fichiers supprimés sont : ",set(listeAncienne)-set(listeNouvelle))
    print("les fichiers ajoutés sont : ", set(listeNouvelle)-set(listeAncienne))
    for i in set(listeNouvelle)-set(listeAncienne) :
        logs.newFileLog(logfile,i)
    for i in set(listeAncienne)-set(listeNouvelle):
        logs.supprFileLog(logfile,i)

def recur(liste1 : list,liste2 : list,logfile):
    listeFichier1 = list()
    listeDossier1 = list()
    listeFichier2 = list()
    listeDossier2 = list()
    for i in liste1 :
        if not isinstance(i[0],list) :
            listeFichier1.append(i[0])
        else :
            listeDossier1.append(i[0])
    for i in liste2 :
        if not isinstance(i[0],list) :
            listeFichier2.append(i[0])
        else :
            listeDossier2.append(i[0])

    comparator(listeFichier1,listeFichier2,logfile)
    for i in listeDossier1:
        for j in listeDossier2 :
            if i[0] == j[0]:
                recur(i[1],j[1],logfile)
                listeDossier1.remove(i)
                listeDossier2.remove(j)
    #nouveaux dossiers
    for i in listeDossier1:
        print(i[0],"nouveau dossier")
        logs.newFolderLog(logfile,i[0])
        recur(listeDossier1,[],logfile)
    #dossiers supprimés
    for i in listeDossier2:
        print(i[0],"dossier supprimé")
        logs.supprFolderLog(logfile,i[0])
        recur([],listeDossier2,logfile)

