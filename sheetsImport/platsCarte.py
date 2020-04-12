import gspread
from oauth2client.service_account import ServiceAccountCredentials

from classes import Plat  # Importation de la classe Plat

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('packages/client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Carte du restaurant").worksheet("Menu")



categories = ["Entree","Plat","Dessert"]

#Création des plats et ajouts à la carte
def ajoutPlats(carte) :
  
  list_nom = sheet.col_values(1)
  list_compo = sheet.col_values(2)
  list_prix = sheet.col_values(3)
  list_cat = sheet.col_values(4)

  for i in range(2,len(list_nom)): 
      plat = Plat.Plat(list_cat[i],list_nom[i],list_compo[i],list_prix[i])
      if(plat.nom != "" ) :
        carte.append(plat)
        
  #PLATS SUR LA CARTE 
  #===================
  '''
  #ENTREE 
  #=======
  saladeChevre = Plat(
    categories[0], 
    nom = "Salade de chèvre chaud",
    composition= ["Salade verte","Cabecou", "miel d'Acacia"],prix= 4)

  assietteCharcut = Plat(
    categories[0], 
    nom = "Assiette de charcuterie", 
    composition = ["Rosette", "Copa", "Jambon de pays", "saucisson"], 
    prix= 4)

  #REPAS
  #======
  daurade = Plat(
    categories[1],
    nom = "Daurade grillée",
    composition = ["Accompagnée de son flan à la courgette"],
    prix = 10)
  

  bavette = Plat(
    categories[1],
    nom = "Bavette",
    composition = ["Sauce au poivre accompagnée de carrottes glacées et riz"],
    prix = 12)
  

  #DESSERT
  #=======
  tiramisu = Plat ( 
    categories[2],
    nom =  "Tiramisu à la framboise", 
    prix = 3)
  

  clafouti = Plat ( 
    categories[2],
    nom =  "Clafoutit aux abricots",  
    prix = 3)
  

  ileFlottante = Plat ( 
    categories[2],
    nom =  "Ile flottante",  
    prix = 2)
  

  #Ajout des plats à la carte
  carte.append(saladeChevre)
  carte.append(assietteCharcut)

  carte.append(daurade)
  carte.append(bavette)

  carte.append(tiramisu)
  carte.append(clafouti)
  carte.append(ileFlottante)
  '''
 #CARTE DES BOISSONS
 # =================================

  # Soft
  
  #Alcool
  '''
  Sima: Citron, Orange, Pamplemousse   
  Vin Rouge:
  Vin Blanc:
  Rosé:
  Bière:

  #Boissons chaudes
Thés
Chocolat chaud 
Capuccino
Café
Gourmand +1€
'''