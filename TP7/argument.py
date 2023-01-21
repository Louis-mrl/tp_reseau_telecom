import sys 
if __name__ == '__main__': 
    if len(sys.argv) == 1:
        print("Pas assez d'argument")
        sys.exit()
    elif len(sys.argv) > 1:
        for elt in sys.argv: # pour chaque élément de la liste sys.argv 
            print(elt)