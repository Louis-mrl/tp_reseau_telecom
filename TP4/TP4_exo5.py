date=input("entrez une date sous la forme jjmmaaaa: ")
annee = int(date[4:8])
jour = int(date[0:2])
mois = int(date[2:4])

print (f"{jour}/{mois}/{annee}")

msg = "date correcte"
if mois>12 or mois <1:
    msg = "mois hors du calendrier"

if jour <0:
    msg = "jour hors calendrier"
else:
    if mois==1 or mois == 3 or mois== 5 or mois == 7 or mois == 8 or mois == 10 or mois ==12:
        if jour > 31:
            msg = "jour hors calendrier"
    elif mois == 2:
        if ((annee%4==0 and annee%100!=0) or annee%400==0):
            if jour > 29:
                msg = "jour hors calendrier"
        else:
            if jour >28:
                msg = "jour hors calendrier"
    else:
        if jour > 30:
            msg = "jour hors calendrier"

print(msg)