x = float(input("entrez un nombre réél: "))

#test algorithmique classique, 2 valeurs comparées et combinaison logique

if ((x>=2 and x<3) or (x>0 and x<=1) or (x>=-10 and x<=-2)):
    print (f"{x} appartient à I [2;3[ U ]0;1] U [-10;-2]")
else:
    print(f"{x} n'appartient pas à I [2;3[ U ]0;1] U [-10;-2]")

# test version python

if (2<=x<3 or 0<x<=1 or -10<=x<=-2):
    print(f"{x} appartient à I [2;3[ U ]0;1] U [-10;-2]")
else:
    print(f"{x} n'appartient pas à I [2;3[ U ]0;1] U [-10;-2]")
