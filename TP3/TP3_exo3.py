# nombre mystère

from random import randint
count = 1
x=randint(1,100)
print("vous devez trouver un nombre entre 0 et 100")
var = int(input("saisir un entier"))
while (var != x):
    if var > x:
        print(f"{var} est plus grand que le nombre à trouver")
    else:
        print(f"{var} est plus petit que le nombre à trouver")
    count +=1
    var = int(input("saisir un entier"))

print (f"vous avez trouver {x} en {count} essai")