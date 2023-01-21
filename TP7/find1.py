import os
import sys

def affiche(repertoire):
        for entry in os.listdir(repertoire):
            print(entry)


def help_function():
    print("Usage: python find1.py [répertoire]")

if len(sys.argv) != 2:
    help_function()
    sys.exit()

directory = sys.argv[1]

if not os.path.exists(directory):
    print("Erreur: le répertoire n'existe pas.")
    help_function()
    sys.exit()
else:
    affiche(directory)