BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("nombre de personnes: "))

fromage2 = fromage*nbConvives/BASE
eau2 = eau*nbConvives/BASE
ail2 = ail*nbConvives/BASE
pain2 = pain*nbConvives/BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut: \n - {fromage2} gr de fromage "
      f"\n - {eau2} dl d'eau \n - {ail2} gousse(s) d'ail \n - {pain2} gr de pain")
