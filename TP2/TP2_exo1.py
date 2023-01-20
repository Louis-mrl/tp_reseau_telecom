x = int(input("entrez x: "))
y = int(input("entrez y: "))

print (f"avant permutation  \n x : {x} \n y: {y}")

# méthode algorithmique classique
temp = x
x = y
y = temp

print (f"aprés une première permutation  \n x : {x} \n y: {y}")

#méthode python

x,y = y,x

print (f"aprés une seconde permutation  \n x : {x} \n y: {y}")

