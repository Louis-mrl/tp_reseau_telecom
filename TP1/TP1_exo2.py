jours = int(input("donner un jour en chiffre: "))
heures = int(input("donner le nombre d'heure: "))
minutes = int(input("donner le nombre de minutes: "))

temps =  (jours*24+heures)*60+minutes

print(f"le nombre de minutes écoulées depuis {jours} jour {heures} heures {minutes} minutes est de {temps}")
