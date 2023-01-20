a=input("Entrez la premiere  valeur : ")
b=input("Entrez la deuxieme  valeur : ")
c=input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
# *******************************************
# * Completez le programme a partir d'ici.
# *******************************************

temp  =  a
a = c
c = b
b = temp

print(f"Les valeurs permutées sont : a ={a} b = {b} et c = {c}")

# méthode python

a,b,c = c,a,b


# *******************************************
# * Ne rien modifier apres cette ligne.
# *******************************************


print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)