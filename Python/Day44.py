#Storing a information of a person

listOfperson = []

def prettyPrint():
  print()
  for row in listOfperson:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()
  print()


while True:
  menu = input("Add or Remove?:" )
  if (menu.strip().lower()[0] == "a"):
      name = input("Your name: ")
      major = input("Your major: ")
      place = input("Your place: ")
      color = input("Favorite color: ")
      
      row = [name, major, place, color]

      listOfperson.append(row)
  else: 
      name = input("What do you want to remove? : ")
      for row in listOfperson:
         if name in row:
            listOfperson.remove(row)
            

  prettyPrint()  


