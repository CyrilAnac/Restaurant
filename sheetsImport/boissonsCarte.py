import gspread
from oauth2client.service_account import ServiceAccountCredentials

from classes import Boisson
 # Importation de la classe Plat

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('packages/client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Carte du restaurant").worksheet("Boissons")



categories = ["ALCOOLS","SOFT","BOISSONS CHAUDES", "COCKTAIL APERITIF"]

#Création des plats et ajouts à la carte
def ajoutBoisson(carte) :
  
  list_nom = sheet.col_values(1)
  list_compo = sheet.col_values(2)
  list_prix = sheet.col_values(3)
  list_cat = sheet.col_values(4)

  for i in range(2,len(list_nom)): 
      boisson = Boisson.Boisson(list_cat[i],list_nom[i],list_compo[i],list_prix[i])
      if(boisson.nom != "" ) :
        carte.append(boisson)