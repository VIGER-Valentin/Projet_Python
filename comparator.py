import logs
def comparator(listeNouvelle : list ,listeAncienne : list,logfile) -> None :
    print("Les fichiers supprimés sont : ",set(listeAncienne)-set(listeNouvelle))
    print("les fichiers ajoutés sont : ", set(listeNouvelle)-set(listeAncienne))
    for i in set(listeNouvelle)-set(listeAncienne) :
        logs.newFileLog(logfile,i)
    for i in set(listeNouvelle)-set(listeAncienne):
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
                recur(i[1],j[1])
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

liste1 = [(['F:\\Documents\\Administratif\\Auto_Entreprise', [('F:\\Documents\\Administratif\\Auto_Entreprise\\Casier judiciaire.jpeg', 'Sat Oct  7 16:38:58 2017'), ('F:\\Documents\\Administratif\\Auto_Entreprise\\dossier_C59062985548 (1).pdf', 'Tue Oct 24 10:33:52 2017'), ('F:\\Documents\\Administratif\\Auto_Entreprise\\Déclaration de non condamnation.pdf', 'Tue Oct 24 11:47:54 2017'), ('F:\\Documents\\Administratif\\Auto_Entreprise\\immatriculation.jpg', 'Thu Dec  7 11:57:20 2017')]], 'Thu Aug 23 15:43:35 2018'), ('F:\\Documents\\Administratif\\Arnaud certificat de participation à la journée Defence et cito.pdf', 'Sat Oct  7 16:01:30 2017'), ('F:\\Documents\\Administratif\\Avis echeance LOYER Arnaud Lagadec (1).pdf', 'Sat Oct  7 16:00:44 2017'), ('F:\\Documents\\Administratif\\carte_d_identite.jpg', 'Sun Oct  8 14:14:30 2017'), ('F:\\Documents\\Administratif\\ID 2.jpeg', 'Sat Oct  7 16:48:34 2017'), ('F:\\Documents\\Administratif\\ID.jpeg', 'Sat Oct  7 16:48:02 2017'), ('F:\\Documents\\Administratif\\id.pdf', 'Tue Oct 24 11:40:58 2017'), ('F:\\Documents\\Administratif\\ordonnance ophtalmo arnaud.pdf', 'Sat Oct  7 16:01:50 2017'), ('F:\\Documents\\Administratif\\Recensement.jpeg', 'Sat Oct  7 16:37:14 2017')]
liste2 = [];
recur(liste1,liste2,"lol")
