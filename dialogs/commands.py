
from classes import Command
import time




nomReserve = ["Anaclet", "Buso", "Guthrie"]
# Verifie si la personne a reservé
def verificationReservation(nomSaisie):
    trouve = False

    #boucle sur le tableau des personnes qui ont reservés
    for nom in nomReserve:
        if nom == nomSaisie:
            trouve = True

    return trouve

class reserveOui:
    def __init__(self,title) :
        self.title = title

    def action(self) : 
        nomSaisie = input('A quel nom ? : ')
        reserve = verificationReservation(nomSaisie)
        if (reserve):
            print('Très bien ' + nomSaisie + ' figure dans ma liste')
            print("Je vous accompagne a votre table..")
            time.sleep(3)
        else:
            print('Désolé ' + nomSaisie + ' n\'apparait pas dans ma liste')


class reserveNon :
    def __init__(self,title) :
        self.title = title

    def action(self) : 
        combien = input('Combien êtes vous ? : ')
        print('D\'accord, il y a une table de ' + combien + ' personnes ici')
        time.sleep(2)


    
class reserveAutrejour:
    def __init__(self,title) :
        self.title = title

    def action(self) : 
        print("Ah d'accord, mais pour l'instant nous sommes en travaux!")
