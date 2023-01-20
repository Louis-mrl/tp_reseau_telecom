# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)  
def ajouter_elt(lst:list=[0,1,2], elt=3) -> list:
    lst.append(elt)  
    return lst


# print(ajouter_elt()) renvois une liste contenant [0, 1, 2, 3]

lst = [1, 2, 3, 4]
lst2 = ajouter_elt(lst)
print(id(lst))
print(id(lst2))

#  on s'appersois que les 2 listes on le même id, cela veux dire qu'elles possedent la même adresse mémoire, elles sont donc similaires


def ajouter_carac(ch='abc', elt='d'):
    return ch+elt

# print(ajouter_carac()) renvois le string "abcde"

string = "123"
string2 = ajouter_carac(string)
print(id(string))
print(id(string2))

# Les deux strings n'ont pas le meme id, ils ne sont donc pas similaires