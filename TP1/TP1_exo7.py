from random import randint

alea = randint(0, 100)

print("alea", alea)
if alea < 100*2/3:
    print("pile")
else:
    print("face")
