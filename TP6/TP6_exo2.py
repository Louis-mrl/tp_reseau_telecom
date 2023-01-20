# déclaration de la fonction ajouter_elt(liste, elt):  
def ajouter_elt(lst:list, elt) -> list:  
    lst.append(elt)  
    return lst

lst1 = [0, 1, 2]

lst2 = ajouter_elt(lst1, len(lst1))


print(f"lst1 : {id(lst1), type(lst1)}")
for item in lst1:
    print(id(item), type(item))

print(f"lst1 : {id(lst2), type(lst2)}")
for item in lst2:
    print(id(item), type(item))

# on observe que les listes et les objets a l'intérieur des listes on le meme id