def colorChange(color):
  if color == "r":
    print('\033[31m', end="")
  elif color == "b"  :
    print('\033[34m', end="")
  elif color == "g"  :
    print('\033[32m', end="")
  elif color == "o"  :
    print('\033[38;5;214m', end="")  
  elif color == "y"  :
    print('\033[33m', end="")  
  elif color == "p"  :
    print('\033[35m', end="")  
  elif color == "w"  :
    print('\033[0m', end="")  
       

user = input("What sentence do you want to rainbow-ising?\n> ")
for letter in user:
  colorChange(letter.lower())
  print(letter, end="")
    
print()