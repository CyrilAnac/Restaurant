print (' coucou, comment tu t appelles? ')
name= input ()
print ( ' Ah, ' + name + ' joli prénom !')
print (' est ce que tu m aimes? ')
reponse= input()

if reponse== "oui" :
 print (' oh moi aussi !')
if reponse== "non":
  print ( 'dommage, je t aimais beaucoup' +name+ ' tu veux qu on reste amis? ')
  reponse2= input ()
  if reponse2 == "oui":
    print ( 'super allons au cinéma voir le seigneur des anneaux, demain ça te plairait ?')
    reponse3= input ()
    if reponse3 == "oui":
      print ( "parfait, a demain")
    if reponse3== "non":
      print ( " tu proposes quel jour? ")
      reponse4= input ()
      print ( 'c\'est bon pour moi')
  if reponse2 == "non":
    print (' alors aurevoir, tu me brises le coeur ')

'''
Les idées pour le restaurants: 
*Faire des formules, 
  entrées+plat à 12€
  plat+dessert à 10€
  entrée + plat+dessert à 16 €
* Laisser le choix au "joueur" de ses actions exemple         commander ou demander des infos à la serveuse sur les plats   ou demander l'addition
*Pour les commande le laisser parler, pas demander à chauque fois en entrée, en plat etc... Si il a pas pris de déssert quand on embarque son plat on lui demande si il est sur de pas vouloir de déssert
'''