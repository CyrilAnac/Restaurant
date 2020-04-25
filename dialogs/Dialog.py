from dialogs import commands
class Dialog:
  

  def __init__(self) :
    self.listCommand = []
    self.nbCmd = 0

  def addCmd(self,command) :
    self.listCommand.append(command)
    self.nbCmd += 1

  def removeCmd(self,command) :
    self.listCommand.remove(command)
    self.nbCmd -= 1

  def prt(self) :
    print("-------------------")
    for x in range(0,self.nbCmd) :
      print(str(x+1)+"- "+self.listCommand[x].title) 
    print("-------------------")

    res = 0
    try:
      res = int(input("> "))
    except ValueError:
      print("(Tapez un nombre)")
    while(res< 1 or res > self.nbCmd) :
      print("Ce choix n'est pas dans la liste !")
      try:
        res = int(input("> "))
      except ValueError:
        print("(Tapez un nombre)")

    com = self.listCommand[res-1]
    self.listCommand.clear()
    self.nbCmd = 0
    
    return com.action()
    
    