import os,time
listOfNames = []

def printName():
  print()
  for i in listOfNames:
    print(i)

while True:
  os.system("clear")
  askUserName = input("\nFirst name : ").strip().capitalize()
  askUserSurname = input("Last name : ").strip().capitalize()
  print()
  userName = f"{askUserName} {askUserSurname}"
  if userName not in listOfNames:
    listOfNames.append(userName)
  else:
    print("ERROR : DUPLICATE NAME")  
  printName()  
  time.sleep(1)
  
