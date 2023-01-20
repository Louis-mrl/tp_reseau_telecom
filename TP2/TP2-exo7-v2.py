#location de vélo méthode avec des boucles

heuredebut = int(input("entrez l'heure de début de la location (un entier): "))
heurefin = int(input("entrez l'heure de fin de la location (un entier): "))

while (heuredebut<0 or heuredebut >24 or heurefin<0 or heurefin> 24 or heurefin <= heuredebut):
    if heuredebut<0 or heuredebut >24 or heurefin<0 or heurefin> 24:
        print("les heures de location doivent être comprises entre 0 et 24 !")
    if heuredebut == heurefin:
        print("Attention ! L'heure de fin est identique à l'heure de début.")
    if heuredebut > heurefin :
        print("Attention ! Le début de la location est aprés la fin …")

    heuredebut = int(input("entrez l'heure de début de la location (un entier): "))
    heurefin = int(input("entrez l'heure de fin de la location (un entier): "))

h1=0
h2=0

for i in range(heuredebut,heurefin,1):
    if i<7 or i>=17:
        h1+=1
    else:
        h2+=1

print("vous avez loué votre vélo pendant")
if (h1 > 0):
    print(f"{h1} heure(s) au tarif horaire de 1.0 euro")
if (h2 > 0):
    print(f"{h2} heure(s) au tarif horaire de 2.0 euro")
print (f"Le montant total à payer est de {h1+h2*2} euro(s)")