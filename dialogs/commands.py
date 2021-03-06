
import time
from sheetsImport import platsCarte,boissonsCarte
import colorama as cr
# Initialise colorama and make it so that the colours auto reset
cr.init(autoreset=True)


#Permet la vérification de la saisie, qui appartient à la carte ou non
def verificationPlat(saisie, carte):
    trouve = False

    # Boucle sur tout les noms de plats
    for plat in carte:
        if saisie == plat.nom:
            platPris = plat.nom
            trouve = True

    if trouve:
        print(platPris + ", c'est noté")
    else:
        print('Désolé,ce plat n\'existe pas!')
    return trouve


# Permet l'affichage complet de la carte
def afficherLaCarte(carte):
    for cat in platsCarte.categories:
        print()
        print(cat + " :")
        print("---------------")
        for plat in carte:
            if (plat.categorie == cat
                ):  #Si le plat appartient à la bonne catégorie, on l'affiche
                print('-> ' + f"{cr.Fore.CYAN}" + plat.nom + '    ' +
                      str(plat.prix) + '€')
                print(f"{cr.Fore.MAGENTA}" + "\033[3m" + plat.composition)
                print()


def afficherBoisson(carte):
    for cat in boissonsCarte.categories:
        print()
        print(cat + " :")
        print("---------------")
        for boisson in carte:
            if (
                    boisson.categorie == cat
            ):  #Si la boisson appartient à la bonne catégorie, on l'affiche
                print('-> ' + f"{cr.Fore.CYAN}" + boisson.nom + '    ' +
                      str(boisson.prix) + '€')
                print(f"{cr.Fore.MAGENTA}" + "\033[3m" + boisson.composition)
                print()




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

class AperitifOui:
    def __init__(self, title, carte) :
        self.title = title
        self.carte = carte
    
    def action(self) :
      print("Voici la carte des boissons je vous laisse choisir!")
      time.sleep (3)
      afficherBoisson(self.carte)
      time.sleep (5)

      return True 
      
class ChoixNon :
    def __init__(self, title, dialog, carte) :
        self.title = title  
        self.dialog = dialog 
        self.carte = carte     

    def action(self) :
        print('Je reviens dans un instant')
        time.sleep(3)      
        print('Avez vous fait votre choix?')
        self.dialog.addCmd(ChoixOui("Oui", self.carte))
        self.dialog.addCmd(ChoixNon("Non pas encore", self.dialog))
        self.dialog.prt()

class ChoixOui :
    def __init__(self, title, carte) :
        self.title = title 
        self.carte = carte            
    
    def action(self) :
        boisson = input("Que désirez vous boire ?\n")
        verificationPlat(boisson, self.carte)
        print('Je vous apporte votre ' + boisson)
        time.sleep(3)
        print ('Voici votre ' + boisson)
        time.sleep(5)
        
  
class AperitifNon:
   def __init__(self, title, carte) :
       self.title = title 
       self.carte = carte

   def action(self) :
     print("Voici le menu ainsi que la carte des boissons, je vous laisse réfléchir!")
     afficherLaCarte(self.carte)
     afficherBoisson(self.carte)

class ManqueSel:
    def __init__(self, title) :
        self.title = title
    
    def action(self) :
      print("Pourions nous avoir du sel s'il vous plaît")
      time.sleep (1)
      print("Oui biensûr!")
      time.sleep(2)
      print("Voici du sel! Bon appétit!")

class ManqueEau:
    def __init__(self, title) :
        self.title = title

    def action(self) :
      print("Une carafe d'eau s'il vous plaît")
      time.sleep(1)
      print("Je vous apporte ça tout de suite")
      time.sleep(2)
      print("Voici de l'eau, bon appétit!")
      time.sleep(5)

class ManquePain: 
    def __init__(self, title) :
        self.title = title

    def action(self) :
      print("Pourrions-nous avoir du pain s'il vous plaît?")
      time.sleep(1)
      print("Je vous apporte ça")
      time.sleep(2)
      print("Voici votre pain, bon appétit!")
      time.sleep(5)

class RenvoyerCuisine:
    def __init__(self, title) :
        self.title = title
    
    def action(self) :
      print("Motif?")
      motif = input()
      print("Très bien, je renvoie ce plat en cuisine pour " + motif)
      print("Je vous un apporte un autre")
      time.sleep(3)
      print("Voici votre nouveau plat, bon appétit!")
      time.sleep(5)

# class Rien:
#     def __init__(self, title) :
#         self.title = title
    
#     def action(self) :
#       print()



