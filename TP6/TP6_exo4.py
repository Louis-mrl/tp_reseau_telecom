import random  

def generer(nbr:int, vmin:int, vmax:int) -> list:
    """Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs comprises entre 'vmin' et 'vmax'"""
    return [random.randint(vmin, vmax) for i in range(nbr)]


def combienInferieur(table:list, vseuil:int) -> int:
    """Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs d'un tableau 'table' inférieures à la valeur 'vseuil' """
    return sum(1 for nombre in table if nombre < vseuil)

nb = 100  
print(f"Générer {nb} nombres entiers entre 0 et 100") 
tab = generer(nb, 0, 100)  
tab.sort()  
print(tab)  
total = combienInferieur(tab, 25)  
print(f"Il y en a {total} inférieurs à 25") 
 
 
