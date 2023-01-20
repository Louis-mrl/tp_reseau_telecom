names = []

for i in range(2):
    name = input("Entrez le nom et le prénom de la personne : ").split()
    names.append({"first_name": name[0].capitalize(), "last_name": name[1].upper()})

names = sorted(names, key=lambda x: (x["last_name"], x["first_name"]))

for name in names:
    print(name["first_name"], name["last_name"])
