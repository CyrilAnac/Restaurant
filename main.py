
import platsCarte 
import boissonsCarte
import time
import random
import colorama as cr
# Initialise colorama and make it so that the colours auto reset
cr.init(autoreset=True)

print(f"{cr.Fore.BLACK}BLACK")
print(f"{cr.Fore.BLUE}BLUE")
print(f"{cr.Fore.CYAN}CYAN")
print(f"{cr.Fore.GREEN}GREEN")
print(f"{cr.Fore.MAGENTA}MAGENTA")
print(f"{cr.Fore.RED}RED")
print(f"{cr.Fore.WHITE}WHITE")
print(f"{cr.Fore.YELLOW}YELLOW")


# Permet l'affichage complet de la carte
def afficherLaCarte() :
  for cat in platsCarte.categories : 
    print()
    print(cat+" :")
    print("---------------")
    for plat in laCarte :
      if(plat.categorie == cat) : #Si le plat appartient à la bonne catégorie, on l'affiche
        print('-> '+f"{cr.Fore.CYAN}"+plat.nom+'    '+str(plat.prix)+'€')
        print(f"{cr.Fore.MAGENTA}"+"\033[3m"+plat.composition)
        print()

def afficherBoisson() :
  for cat in boissonsCarte.categories : 
    print()
    print(cat+" :")
    print("---------------")
    for boisson in laCarte :
      if(boisson.categorie == cat) : #Si la boisson appartient à la bonne catégorie, on l'affiche
        print('-> '+f"{cr.Fore.CYAN}"+boisson.nom+'    '+str(boisson.prix)+'€')
        print(f"{cr.Fore.MAGENTA}"+"\033[3m"+boisson.composition)
        print()

    
#Permet la vérification de la saisie, qui appartient à la carte ou non
def verificationPlat(saisie) :
  trouve= False

  # Boucle sur tout les noms de plats
  for plat in laCarte :
    if saisie == plat.nom :
       platPris = plat.nom
       trouve = True


  if trouve:
    print(platPris+", c'est noté")
  else:
    print('Désolé,ce plat n\'existe pas!')
  return trouve


# Permet de trouver le plat en fonction de la saisie
def platPris(saisie) : 
  for plat in laCarte :
    if saisie == plat.nom :
       return plat
  
# Verifie si la personne a reservé 
def verificationReservation(nomSaisie) :
  trouve=False

  #boucle sur le tableau des personnes qui ont reservés
  for nom in nomReserve :
    if nom == nomSaisie :
      trouve = True
 
  return trouve


def addition(listePlats):
  prixTotal = 0

  for plat in listePlats :
      prixTotal += int(plat.prix)

  return prixTotal

# DECLARATIONS
#==============
laCarte = []
platsCarte.ajoutPlats(laCarte)
#boissonsCarte.ajoutBoisson(laCarte)

nomReserve = ["Anaclet","Buso","Guthrie"]
nombreClient = random.randint(10,40)
NB_PLACES_MAX = 40
platsCommandes = [] 


#BEGIIIN
print("-----------------------------------------------")
print("|                                             |")
print("|         Le Resto de Cyril et Luna <3        |")
print("|                                             |")
print("-----------------------------------------------")
print(" Bonjour et bienvenus au réstaurant de Cyril et Luna!\n\n")

# Reservation 
#_________________________________________
reserve= False
reservation = input("Avez vous réservé ? : ")
if reservation == "oui":
  nomSaisie = input( 'A quel nom ? : ')
  reserve = verificationReservation(nomSaisie) 
  if(reserve) :
    print('Très bien '+nomSaisie+ ' figure dans ma liste')
    print("Je vous accompagne a votre table..")
    time.sleep(3)
  else :
    print('Désolé '+ nomSaisie+ ' n\'apparait pas dans ma liste')

#Si il n'y a pas eu de reservation
if(not reserve) : 
  combien = input ('Combien êtes vous ? : ')
  # TODO: Verification si il y a de la place
  print ('D\'accord, il y a une table de ' + combien+' personnes ici')
  time.sleep (2)


print ("Voici la carte, je vous laisse réfléchir quelques instants.")
time.sleep (3)
#afficherBoisson()
afficherLaCarte()
time.sleep (5)

#BUG
choix=input('Avez-vous choisi ? : ')
#Tant que la réponse n'est pas oui, on repose la question
while(choix != "oui") :
  print ('Je reviens dans un instant')
  time.sleep (3)
  choix=input('Avez-vous choisi ? : ')


#Tant que la réponse n'est pas dans la carte, on redemande ce qu'il veut en entrée
entree= input("Que désirez vous en entrée ?\n")
while (not verificationPlat(entree)):
  entree=input ('Que désirez vous en entrée ?\n')
  
plat = platPris(entree)
platsCommandes.append(plat)

print ("En plat principal?")
plat= input()
while (not verificationPlat(plat)):
   plat=input ('Que désirez vous en plat')
platsCommandes.append(platPris(plat))

print ("Un déssert ? ")
dessert=input()
if dessert == "oui":
    print('lequel?')
    queldessert=input()
    while (not verificationPlat(queldessert)):
      queldessert=input ('Que désirez vous en dessert')
    platsCommandes.append(platPris(queldessert))
    print (' très bien ')

else :
  print('c\'est noté, je vous apporte ça!')

time.sleep(5)
print('Voici votre ' + entree)
time.sleep (10)
print('Avez vous terminez?')
finientree=input()
while(finientree != "oui") :
  print ('Je reviens dans un instant')
  time.sleep (5)
  finientree= input('Avez vous terminé?')
print ('je vous débarrasse et vous apporte votre plat tout de suite')
time.sleep(3) 
print ('voici votre ' + plat)
time.sleep (10)
print('Avez vous terminez?')
finiplat=input()
while(finiplat != "oui") :
  print ('Je reviens dans un instant')
  time.sleep (5)
  finiplat= input('Avez vous terminé?')

dessertTrouve = False
for plat in platsCommandes : 
  if plat.categorie == "Dessert" :
    dessertTrouve = True

if(dessertTrouve) :
  print('Je vous apporte votre dessert tout de suite')
  time.sleep(3)
  print('voici votre ' +queldessert)
  time.sleep (3)

print ('Voici l\'addition') 
prix = addition (platsCommandes)
print ("cela vous coutera "+str(prix)+" euros")


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


  



