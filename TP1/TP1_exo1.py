nom = "ALBERT"
prenom = "Arnauld"
math=12.1
anglais = 8.5
info = 17.2
promotion = 1993

moy = (math+anglais+info)/3

print(f"math est de type {type(math)} et vaut {math}")
print(f"anglais est de type {type(anglais)} et vaut {anglais}")
print(f"promotion est de type {type(promotion)} et vaut {promotion}")

print(f"La moyenne des notes vaut {moy:.2f}")

print(f"l'étudiant {prenom} {nom} de la promotion {promotion} a une moyenne de {moy}")