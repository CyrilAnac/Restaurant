
class Plat:
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
  
  #retourne une caine de caractère avec la composition du plat
  '''
  def getComposition(self) :
    chaine = ""
    for elmt in self.composition :
      chaine += (elmt+', ')
      #chaine += elmt+", "
    return chaine
  '''

