temps = int(input("nombre de minutes écoulées depuis une date donnée: "))


heures = int(temps /60)
minutes = temps - heures*60
jours = int(heures / 24)
heures = heures - jours*24
print(f" il y a {jours} jours {heures} heures et {minutes} minutes écoulé depuis les {temps} minutes")