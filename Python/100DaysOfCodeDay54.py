import time,os,random
myTodo = []
fileExists = True
try:
  f = open("Todo list Management System", "r")
  myTodo = eval(f.read())
  f.close()
except:
  fileExists = False 

def prettyPrint():
    for row in myTodo:
      print(f"{row[0]:^15} {row[1]:^15} {row[2]:^15} ")
    print()

def add():
  os.system("clear")
  time.sleep(1)
  print()
  print("ADD\n")
  task = input("Add your task: ").title()
  date = input("When is it due?: ")
  priority = input("How important?[very,moderate,less]: ").capitalize()
  row = [task,date,priority]
  myTodo.append(row)
  print("\nADDED")
  time.sleep(1)
  os.system("clear")

def view():
  print()
  choice = int(input("1.View all\n2.View by priority\n> "))
  if choice == 1:
    prettyPrint() 
  elif choice == 2:
    specificTodo = input("View your todo according to your priority.\nEnter your order of priority[very/moderate/less]\n> ").capitalize()
    for row in myTodo:
      if specificTodo in row:
        for item in row:
          print(f"{item:^15}", end = " ")
        print()  
    print()  
  if not myTodo:
    print("Add your todos to view")  

def remove():
  os.system("clear")
  time.sleep(1)
  print("\nREMOVE\n")
  delete = input("Enter your task to remove:\n> ").title()
  for row in myTodo:
    if delete in row:
      myTodo.remove(row)
      print("\nYour Updated TODO list:\n")
      prettyPrint()
  print()    
  os.system("clear")
  time.sleep(1)
      
def edit():
  os.system("clear")
  time.sleep(1)
  print("\nEDIT\n")
  found = False
  find = input("Enter your todo to edit:\n> ")
  for row in myTodo:
    if find in row:
      found = True
  if not found:
    print("Not in the list.\n")    
    return
  for row in myTodo:
    if find in row:
      myTodo.remove(row)
  print("ADD\n")
  task = input("Add your task: ").title()
  date = input("When is it due?: ")
  priority = input("How important?[very,moderate,less]: ").capitalize()
  row = [task,date,priority]
  myTodo.append(row)
  print("\nADDED")
  time.sleep(1)
  os.system("clear")  

while True:
  print("\nToDO list Management System")
  print()
  menu = int(input("1.Add\n2.View\n3.Remove\n4.Edit\n5.Exit\n\n> "))
  if menu == 1:
    add()
  elif menu == 2:
    view()  
  elif menu == 3:
    remove()
  elif menu == 4:
    edit()
  elif menu == 5:
    break  
  else:
    print("Wrong input")  
    input("Press enter to continue..")

  if fileExists:
    try:
      os.mkdir("Backups") 
    except:
      pass   
  
  name = f"backups{random.randint(1,100000000)}.txt"
  os.popen(f"cp Todos Backups/{name}")
  f = open("Todos", "w")    
  f.write(str(myTodo))
  f.close()