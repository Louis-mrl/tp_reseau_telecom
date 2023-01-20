# compte à rebours
from time import sleep
n=-1
while n<0:
    n=int(input("saisir un nombre entier positif "))

""" première méthode avec un while """
while n>=0:
    print(n)
    sleep(0.5)
    n-=1


""" seconde méthode avec un for """
n=-1
while n<0:
    n=int(input("saisir un nombre entier positif "))

for i in range (n,-1,-1):
    print(i)
    sleep(0.5)
