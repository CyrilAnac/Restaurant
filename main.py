


import dialogs.commands as cd
from dialogs.Dialog import Dialog
import time
from sheetsImport import platsCarte,boissonsCarte
import random
import colorama as cr
# Initialise colorama and make it so that the colours auto reset
cr.init(autoreset=True)




#Permet la vérification de la saisie, qui appartient à la carte ou non
def verificationPlat(saisie):
    trouve = False

    # Boucle sur tout les noms de plats
    for plat in laCarte:
        if saisie == plat.nom:
            platPris = plat.nom
            trouve = True

    if trouve:
        print(platPris + ", c'est noté")
    else:
        print('Désolé,ce plat n\'existe pas!')
    return trouve


# Permet de trouver le plat en fonction de la saisie
def platPris(saisie):
    for plat in laCarte:
        if saisie == plat.nom:
            return plat


def addition(listePlats):
    prixTotal = 0

    for plat in listePlats:
        prixTotal += int(plat.prix)

    return prixTotal

# DECLARATIONS
#==============
laCarte = []
platsCarte.ajoutPlats(laCarte)
boissonsCarte.ajoutBoisson(laCarte)
nombreClient = random.randint(10, 40)
NB_PLACES_MAX = 40
platsCommandes = []
dl = Dialog()


#BEGIIIN
print("-----------------------------------------------")
print("|                                             |")
print("|         Le Resto de Cyril et Luna <3        |")
print("|                                             |")
print("-----------------------------------------------")
print(" Bonjour et bienvenus au restaurant de Cyril et Luna!\n\n")



# Reservation
#----------------------------------------
print("Avez vous réservé ? : ")
dl.addCmd(cd.reserveOui("oui"))
dl.addCmd(cd.reserveNon("non"))  # variable nb de personne
dl.addCmd(cd.reserveAutrejour("Nous voudrions réserver pour un autre jour"))
dl.prt()

# Aperitif
#----------------------------------------
print("Souhaitez vous un apéritif ?")
dl.addCmd(cd.AperitifOui("oui", laCarte))
dl.addCmd(cd.AperitifNon("non", laCarte))

if dl.prt() : # Oui pour un aperitif
        print('Avez-vous choisi ? : ')
        dl.addCmd(cd.ChoixOui("Oui"))
        dl.addCmd(cd.ChoixNon("Non pas encore", dl))
        dl.prt()
  

#         choix = input('Avez-vous terminé ? : ')
# #Tant que la réponse n'est pas oui, on repose la question
#         while (choix != "oui"):
#             print('Je reviens dans un instant')
#             time.sleep(3)
#             choix = input('Avez-vous terminé ? : ')
#             print("Voici le menu, je vous laisse réfléchir")
#             afficherLaCarte(self.carte)



choix = input('Avez-vous choisi ? : ')
#Tant que la réponse n'est pas oui, on repose la question
while (choix != "oui"):
    print('Je reviens dans un instant')
    time.sleep(3)
    choix = input('Avez-vous choisi ? : ')

#Tant que la réponse n'est pas dans la carte, on redemande ce qu'il veut en entrée
entree = input("Que désirez vous en entrée ?\n")
while (not verificationPlat(entree)):
    entree = input('Que désirez vous en entrée ?\n')

plat = platPris(entree)
platsCommandes.append(plat)

print("En plat principal?")
plat = input()
while (not verificationPlat(plat)):
    plat = input('Que désirez vous en plat')
platsCommandes.append(platPris(plat))

print("Un déssert ? ")
dessert = input()
if dessert == "oui":
    print('lequel?')
    queldessert = input()
    while (not verificationPlat(queldessert)):
        queldessert = input('Que désirez vous en dessert')
    platsCommandes.append(platPris(queldessert))
    print(' très bien ')

else:
    print('c\'est noté, je vous apporte ça!')

time.sleep(5)
print('Voici votre ' + entree)
time.sleep(10)


# Boîte de dialogue
dl.addCmd(cd.ManqueSel("Sel"))
dl.addCmd(cd.ManqueEau("Eau"))
dl.addCmd(cd.ManquePain("Pain"))
dl.addCmd(cd.RenvoyerCuisine("Renvoyer le plat"))
dl.addCmd(cd.Rien("Tout va bien!"))
dl.prt()



print('Avez vous terminé?')
finientree = input()
while (finientree != "oui"):
    print('Je reviens dans un instant')
    time.sleep(5)
    finientree = input('Avez vous terminé?')
print('je vous débarrasse et vous apporte votre plat tout de suite')
time.sleep(3)
print('voici votre ' + plat)
dl.addCmd(cd.ManqueSel("Sel"))
dl.addCmd(cd.ManqueEau("Eau"))
dl.addCmd(cd.ManquePain("Pain"))
dl.addCmd(cd.Rien("Tout va bien!"))
dl.addCmd(cd.RenvoyerCuisine("Renvoyer le plat"))
dl.prt()
time.sleep(10)
print('Avez vous terminez?')
finiplat = input()
while (finiplat != "oui"):
    print('Je reviens dans un instant')
    time.sleep(5)
    finiplat = input('Avez vous terminé?')

dessertTrouve = False
for plat in platsCommandes:
    if plat.categorie == "Dessert":
        dessertTrouve = True

if (dessertTrouve):
    print('Je vous apporte votre dessert tout de suite')
    time.sleep(3)
    print('voici votre ' + queldessert)
    dl.addCmd(cd.ManqueEau("Eau"))
    dl.addCmd(cd.RenvoyerCuisine("Renvoyer le dessert"))
    dl.addCmd(cd.Rien("Tout va bien!"))
    dl.prt()
    time.sleep(3)

print('Voici l\'addition')
prix = addition(platsCommandes)
print("cela vous coutera " + str(prix) + " euros")

# TODO
#==================================
# Demande si le client veut d'autres choses sur sa commande
# "Ca sera tout ?"
# Verifier si il y a assez de place dans le resto pour accueilir des clients
# Afficher le resumé de la commande
# Apport des plats, dans l'ordre du repas..
# Proposé un dessert a la fin ? (si pas commandé)
# Carte des boissons ?

# Combien etes vous ?
#aléatoire entre 1 et 7
# Possible ou non?

#Tenez la carte :
#affichage carte
#attente...
#Que voulez vous?
#...
#miam miam

#l'addition
#merci d'etre venu!
