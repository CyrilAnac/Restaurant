
class Boisson:
  categorie = ""
  nom = ""
  composition = ""
  prix = 0
   

  def __init__(self, categorie, nom, composition=[],prix=0):
    self.nom = nom
    self.prix = prix
    self.categorie = categorie
    self.composition = composition

 

  def __str__(self) :
    return (self.categorie +" : " + self.nom)