count10=0
count1015 = 0
count15=0

for i in range(0,10,1):
    n=-1
    while (n<0 or n>20):
        n=int(input("saisr un entier entre 0 et 20"))
    if n < 10:
        count10+=1
    elif n< 15 :
        count1015 +=1
    else:
        count15 += 1

print(f"nb de valeurs < 10 {count10} \n nb de valeurs entre 10 et 15 {count1015} \n nb de valeurs supérieures {count15}")