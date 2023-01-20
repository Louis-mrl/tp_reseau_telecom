L1 = [0] *3

print(id(L1))

for item in L1:
    print(id(item), type(item))
    # on remarque que les 3 objets on le meme id, on remarque aussi qu'il sont evidement tout les 3 des entier


L1[1] += 1

print(id(L1)) 

for item in L1:
    print(id(item), type(item))
    # on remarque que l'id du deuxieme élément a changé cependant, l'id de la liste n'a pas changé