# calcul de la valeurs moyenne des notes d'étudiants

nbEtudiant= int(input("entrez le nombre d'étudiant: "))
moyenne = 0.0
notes = []

for i in range(0,nbEtudiant,1):
    no=-1
    while (0 > no or no > 20):
        no = float(input(f"Note étudiant [{i+1}]: "))
    notes.append(no)


# le dernier chiffre de range correrspond au pas, il n'est pas nécessaire car implicitement c'est 1
for i in range(0,nbEtudiant):
    moyenne += notes[i]

moyenne = moyenne / len(notes)

print(f"La moyenne des {len(notes)} des étudiants est de {moyenne:.2f}")
print ("numéro de l'étudiant | note | écart avec la moyenne")
for i in range(nbEtudiant):
    print(f"{i+1} | {notes[i]} | {notes[i]-moyenne:.2f}")

