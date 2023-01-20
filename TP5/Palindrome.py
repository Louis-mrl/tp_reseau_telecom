chaine = input("Entrez un mot ou une phrase : ")

caracteres = ["a"]
# retrait des caractères non alphabétiques
for caractere in chaine:
    if caractere in caracteres:
        chaine.pop(caractere)
chaine = chaine.lower()

print(chaine)
# vérification du palindrome
if chaine == chaine[::-1]:
    print("C'est un palindrome!")
else:
    print("Ce n'est pas un palindrome.")