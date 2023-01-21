import os
import sys


listeFichiers = [] 
listeRepertoires = []


def recherche(repertoire):
    if repertoire in listeRepertoires:
        listeRepertoires.pop(repertoire)
    for entry in os.listdir(repertoire):
        path = os.path.join(f"{repertoire}/{entry}")
        if os.path.isdir(path):
            listeRepertoires.append(entry)
        else:
            listeFichiers.append(entry)




def help_function(msg=""):
    print(msg)
    print("Usage: python find1.py [répertoire]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        help_function("pas assez d'arguments")
        sys.exit()
    else:
        directory = sys.argv[1]

        if not os.path.exists(directory):
            help_function("Erreur: le répertoire n'existe pas.")
            sys.exit()
        else:
            recherche(directory)
    
print(listeFichiers)