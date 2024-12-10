import random
characters = {}
computer = ["Micheal Scoot","Sheldon Cooper","Phoebe Buffay", "Phill Dunphy","Rachel Green"]
while True:
  print("\nTOP TRUMPS")
  print("------------")
  print("\nCHARACTERS ^-^\n")
  print("Micheal Scoot\nSheldon Cooper\nPhoebe Buffay\nPhill Dunphy\nRachel Green\n")
  choice = input("Pick your character\n> ")
  computerChoice = random.choice(computer)
  print(f"\nComputer has picked {computerChoice}")
  print()

  options = input("Choose your stat: Intelligence, Speed, Guile and baldness level\n> ").lower()
  if options in ["intelligence", "speed", "guile", "baldness level"]:
    userStat = random.randint(0,200)
    computerStat = random.randint(0,200)
    characters[choice] = {options: userStat}
    characters[computerChoice] = {options: computerStat}
    print()
    print("Your Stat:")
    print(f"{choice}: {userStat}")
    print()
    print("Computer's Stat:")
    print(f"{computerChoice}: {computerStat}")
    print()

    if userStat > computerStat:
      print(f"Your character {choice} has won the TOP TRUMPS")
    elif userStat == computerStat:
      print(f"Opps! {choice} and {computerChoice} are no RIVALS")  
    elif userStat < computerStat:
      print(f"Computer's character '{computerChoice}' has won the TOP TRUMPS")
      print()    
  else:
      print("Invalid Choice. Try Again!!!!")

  

