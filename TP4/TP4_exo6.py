import random

N = int(input("entrez le nombre de valeurs du tableau"))

liste=[]
for i in range(N):
    liste.append(random.randint(0,100))


print(liste)
for j in range(0,N-1,1):
    max = j
    for i in range(j+1,N,1):
        if liste[i]<liste[max]:
            max = i

    temp = liste[max]
    liste[max] = liste[j]
    liste[j] = temp
    print(liste)

# liste.sort()

print("seconde méthode sorted(liste)")

liste=[]
for i in range(N):
    liste.append(random.randint(0,100))
print (sorted(liste))

print("dernière méthode liste.sort()")
print(liste)
liste.sort()

print(liste)
