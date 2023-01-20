binome = ("moi", "moi2")

print(f"l'etudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

#binome[1]=input("votre nouveau binome est")

"""
message d'erreur associé
Traceback (most recent call last):
  File "/Users/nono/Developpement/Pyhton/TP-R107/TP4/TP4_exo7.py", line 5, in <module>
    binome[1]=input("votre nouveau binome est")
TypeError: 'tuple' object does not support item assignment
"""

# del(binome[1])
""" 
message d'erreur associé
Traceback (most recent call last):
  File "/Users/nono/Developpement/Pyhton/TP-R107/TP4/TP4_exo7.py", line 7, in <module>
    del(binome[1])
TypeError: 'tuple' object doesn't support item deletion
"""

""" 
 les tuples sont non mutable, c'est à dire qu'il ne sont plus modifiable une fois créé, contrairement aux listes.
"""