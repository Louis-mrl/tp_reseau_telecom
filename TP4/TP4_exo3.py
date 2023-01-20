nMax = 6

n=7
while(n>nMax):
    n=int(input(f"donnez la taille des vecteurs (<{nMax})"))

v1=[]
v2=[]
print("coordonnées du premier vecteur")
for i in range(n):
    v1.append(float(input(f"V1[{i}]")))

print("coordonnées du second vecteur")
for i in range(n):
    v2.append(float(input(f"V2[{i}]")))

ps=0.0
for i in range(n):
    ps += v1[i]*v2[i]

print(f"Le produit scalaire de v1 et v2 = {ps}")