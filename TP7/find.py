import sys
import os 
 
listeRepertoires = [] 
listeFichiers = [] 


def aide(msg): 
    print(msg) 
    print("usage : find.py -f <path to file> -r <path to repositery>") # affiche le nom du script et comment il faut appeler ce script 
    sys.exit()
 


def recherche(repertoire): 
    # Lister les fichiers du répertoire en vous plaçant dans celui-ci 
    contenuDuRépertoire = os.listdir(...) 
    for elt in repertoire : # pour chaque élément (elt) du répertoire 
        if os.path.isdir(elt): # si c’est un répertoire 
            listeRepertoires.append(repertoire + "/" + elt)  
                
        elif os.path.isfile(elt): # sinon si c’est un fichier 
                listeFichiers.append(repertoire + "/" + elt)  
        else:
            print(f"aucun type trouvé pour {elt}")

if __name__ == '__main__': 
    if (len(sys.argv) == 3) or (len(sys.argv) == 5):
        repertoire = "" 
        fichier = "" 
        for i in range(1,len(sys.argv)): # je recherche les arguments 
            if sys.argv[i] == "-d": 
                repertoire = sys.argv[i+1] 
            elif sys.argv[i] == "-f": 
                fichier = sys.argv[i+1]

        if not os.path.exists(repertoire):# si le repertoire n’existe pas 
            aide("répertoire non trouvé") 
        else: 
            if not os.listdir(repertoire): # si repertoire ou fichier sont vides 
                aide("repertoire est vide") 
            else: 
                recherche(repertoire) 
 
        print(listeFichiers)
        print(listeRepertoires)
        for fiche in listeFichiers : 
            print(fiche)
    else: 
        aide("Mauvais nombre d’arguments") 