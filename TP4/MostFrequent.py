L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# * Completez le programme a partir d'ici.
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * 


max=0
nmax=0

for j in range(len(L1)):
    n=0
    for i in range(len(L1)):
        if (L1[j]==L1[i]):
            n+=1
    if n>nmax:
        nmax = n
        max = j

print(f"L'élément le plus présent est {L1[max]} qui apparait {nmax} fois")

# seconde méthode
max = 0
nmax = L1.count(L1[0])
for j in range(1,len(L1)):
    n = L1.count(L1[j]) # remplace la boucle de parcours de la L1.
    if n> nmax:
        max = j
        nmax = n

print(f"L'élément le plus présent est {L1[max]} qui apparait {nmax} fois")






# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# * Ne rien modifier apres cette ligne.
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *

