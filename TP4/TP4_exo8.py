binome1 ={}

binome1['firstname'] = "Arnauld"
binome1['name'] = "ALBERT"
binome1['promotion'] = 2021
binome1['group'] = "RT113"
binome2 ={}

binome2['firstname'] = "toto"
binome2['name'] = "titi"
binome2['promotion'] = 1975
binome2['group'] = "RT3"

#print(binome1.keys())
#print(binome1.values())

"""
for i in binome1.items():
    print(i)
    print(f"cle : {i[0]} valeur : {i[1]}")
"""
tpx={}
tpx["bin1"] = (binome1,binome2)
tpx["bin2"] = (binome2,binome2)
tpx["bin3"] = (binome1,binome1)

#print(tpx)

for i in tpx.items():
    print(f"Binome : {i[0]}")
    for j in range(len(i[1])):
        msg = ""
        for k in i[1][j].items():
            msg += f"{k[0]} : {k[1]} "
        print (msg)
