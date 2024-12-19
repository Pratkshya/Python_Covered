#CHARACTER CREATION

class character:
  name = None
  health = 100
  mp = 100

  def __init__(self, name):
    self.name = name

  def display(self):
    print()
    print("Character Creation")
    print("*" * 10)
    print(f"""{self.name}\tHP: {self.health}\tMP: {self.mp}\t""")

  def setStats(self, health, mp):
    self.health = health
    self.mp = mp


class player(character):
  nickName = None
  lives = 3

  def __init__(self, nickName):
    self.name = "PLAYER"
    self.nickName = nickName   

  def display(self):
    print()
    print(f"""{self.name}\tHP: {self.health}\tMP: {self.mp}\tNickname: {self.nickName}\tLives: {self.lives}""")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickName} lives on!")
      return True
    else:
      print(f"{self.nickName} has experied!")
      return False
    
penny = player("Queen Penelope")    
penny.display()
print(penny.isAlive())

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def display(self):
    print()
    print(f"""{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}""")    
  
class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "orc"
    self.strength = 200
    self.speed = speed

  def display(self):
    print()
    print(f"""{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}""")    

sheldon = orc(250)
howard = orc(200)

sheldon.display()
howard.display()

class vampire(enemy):
  day = True

  def __init__(self, day):
     self.name = "Vampire"
     self.type = "Vampire"
     self.strength = 130
     self.day = day

  def display(self):
    print()
    print(f"""{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}""")       

draculla = vampire(False)    
draculla.display()