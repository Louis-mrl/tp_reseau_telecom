# saisie de notes

notes = []
coeff = []
somme = 0
coefficient = 0
for i in range(2):
    s1 = input(f"veillez entrer la {i+1} ème note et le coefficient associé :")
    s2 = s1.split(" ")
    print(f"note : {s2[0]} coefficient : {s2[1]}")
    notes.append(float(s2[0]))
    coeff.append(float(s2[1]))
    somme+= float(s2[0])* float(s2[1])
    coefficient += float(s2[1])
moyenne = somme/coefficient

print(f"la moyenne est {moyenne:0.2f}")
valid = True
if moyenne < 10 :
    valid = False

for i in range(len(notes)):
    if notes[i] < 8:
        valid = False

if (valid):
    print("vous êtes admis")
else:
    print("vous n'êtes pas admis")
