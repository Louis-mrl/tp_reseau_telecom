liste=[]

nombre=float(input("vous cherchez la table de multiplication de quel nombre? "))
for i in range (0,10,1):
    liste.append([nombre,i,round(i*nombre,1)])

for i in liste:
    print(f"{i[0]} * {i[1]} = {i[2]}")

print(liste)
