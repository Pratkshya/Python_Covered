import os,time
allItems = []
try:
  f = open("Inventory", "r")
  allItems = eval(f.read())
  f.close()
except:
  pass  

def add():
  time.sleep(1)
  os.system("clear")
  print("\nINVENTORY")
  print("=" * 8)
  userData = input("Add an item: ").capitalize()
  allItems.append(userData)
  print("\nAdded\n")

def view():
  time.sleep(1)
  os.system("clear")
  print("\nINVENTORY")
  print("=" * 8)
  print()
  # seen = set(allItems)
  # for item in seen:
  #   print(f"{item} {allItems.count(item)}")
  # time.sleep(2)

  seen = []
  for item in allItems:
    if item not in seen:
      print(f"{item} {allItems.count(item)}")
      seen.append(item)
    else:
      print("Try again..")  

def remove():
  time.sleep(1)
  os.system("clear")
  print("\nINVENTORY")
  print("=" * 8)
  removeItem = input("Item to remove: ").capitalize()
  if removeItem in allItems:
    allItems.remove(removeItem)
    print("Removed")
  else:
    print(f"{removeItem} not found in the list")    

while True:
  print("\nINVENTORY")
  print("=" * 8)
  menu = int(input("\n1. Add\n2. View\n3. Remove\n> "))
  if menu == 1:
    add()
  elif menu == 2:
    view()
  elif menu == 3:
    remove()  

  f = open("Inventory", "w")    
  f.write(str(allItems))
  f.close()