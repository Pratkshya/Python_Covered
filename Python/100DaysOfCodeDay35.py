import time, os
toDoList = []
def listOfToDos():
  print()
  print("Your list of todos are:\n")
  for item in toDoList:
    print(item)
    print()
while True:
  os.system("clear")
  print()
  print("ToDO List Manager")
  print("Do you want to view, add, remove, edit or delete the todo list?")
  askUser = input("> ")
  if askUser == "add":
    print("What do you want to add?")
    user = input("> ")
    if user in toDoList:
      print(f"{user} is already on the list.")
    else:  
     toDoList.append(user)
  elif askUser == "remove":
    print("What do you want to remove?")
    user = input("> ")
    print(f"Are you sure you want to remove '{user}' from the list [y/n]?")
    userChoice = input("> ")
    if userChoice == "y":  
      if user in toDoList:
        toDoList.remove(user)
        print(f"{user} is removed from the list.")
      else:
        print(f"{user} isn't on the list.")
  elif askUser == "view":
    listOfToDos()
  elif askUser == "edit":
    print("What do you want to edit to remove?")
    user = input("> ")
    if user in toDoList:
      toDoList.remove(user)
      print("What do you want to change it to?")
      user = input("> ")
      toDoList.append(user)
    else:
      print(f"{user} not found on the list") 
  elif askUser == "delete":
    toDoList = []  
    print("Your todo list is now deleted") 
    input("Press enter to continue...")
  time.sleep(1)    
  os.system("clear")

    