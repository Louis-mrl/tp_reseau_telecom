entier = int(input("entrez un nombre entier:"))

if (entier <0):
    msg = "un nombre négatif"
    if (entier%2==0):
        msg += " pair"
    else:
        msg += " impair"
elif entier > 0:
    msg = "un nombre positif"
    if (entier%2==0):
        msg += " pair"
    else:
        msg += " impair"
else:
    msg = "zéro (et il est pair)"

print(f"{entier} est {msg}")