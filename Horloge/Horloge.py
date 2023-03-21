import time
from datetime import datetime


def heure_actuelle():  # Fonction pour afficher l'heure actuelle
    while True:  
        heure = str(datetime.now().time())
        heure = heure[:-7]
        print(heure)
        time.sleep(1)


def afficher_heure():  # Fonction permettant d'afficher l'heure précise
    heure_modifier = (16, 30, 0)  # Permet de choisir l'heure
    heure = heure_modifier[0]  
    minute = heure_modifier[1]
    secondes = heure_modifier[2]
    while True:  
        secondes = secondes + 1
        if secondes == 60:
            secondes = 0
            minute = minute + 1
        if minute == 60:
            minute = 0
            heure = heure + 1
        if heure == 24:
            heure = 0

        heure = str(heure)  
        minute = str(minute)
        secondes = str(secondes)
        if len(secondes) < 2:
            secondes = list(secondes)
            secondes.insert(0, "0")
            secondes = "".join(secondes)
        if len(minute) < 2:
            minutes = list(minute)
            minutes.insert(0, "0")
            minutes = "".join(minute)
        if len(heure) < 2:
            heure = list(heure)
            heure.insert(0, "0")
            heure = "".join(heure)

        
        print(heure+":"+minute+":"+secondes)
        heure = int(heure)
        minute = int(minute)
        secondes = int(secondes)
        time.sleep(1)  


def alarme():  # Fonction concernant l'alarme
    while True: 
        heure = str(datetime.now().time())
        heure = heure[:-7]
        reveil = "20:11:00"  # Valeur a changer pour régler l'heure du réveil
        if reveil == heure:
            print("Il est l'heure de se réveiller !")
            break
        else:
            time.sleep(1)

#heure_actuelle()
#afficher_heure()
alarme()