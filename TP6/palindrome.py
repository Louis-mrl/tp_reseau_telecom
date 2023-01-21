def verification(chaine:list) -> bool:
    """vérification du palindrome"""
    chaine2 = list(reversed(chaine))
    if chaine == chaine2:
        return True
    else:
        return False


def clear_text(string:str) -> list:
    """nétoyer le texte en remplacant les majuscules, accents, espaces, de caractères typographiques et des signes de ponctuations"""
    new_string = []
    for caractere in string:
        if caractere in "êëÉÈ":
            caractere == "e"
        elif caractere in ["?", ",", ".", ";", ":", "'", " "]:
            continue
        elif caractere == "à":
            caractere = "a"
        elif caractere == "ç":
            caractere = "c"
        
        caractere.lower()
        new_string.append(caractere)
    return new_string


if __name__ == "__main__":
    chaine = input("Entrez un mot ou une phrase : ")
    chaine = clear_text(chaine)
    if verification(chaine):
        print("c'est un palindrome !")
    else:
        print("ce n'est pas un palindrome")