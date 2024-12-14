myTodos = []

f = open("Event Planner", "r")
myTodos = eval(f.read())
f.close()


def prettyPrint():
 print()
 for row in myTodos:
  print(f"{row[0]:^15} {row[1]:^15} {row[2]:^15}")
print()  
while True:
  print("\nMood Planner")
  menu = int(input("\n1.ADD\n2.Remove\n> "))
  if menu == 1:
    day = input("Add an event: ").title()
    date = input("Enter the date: ")
    priority = input("How important?: ")

    data = [day, date, priority]
    myTodos.append(data)
    prettyPrint()
    print()

  elif menu == 2:
    print()  
    choice = input("Enter the title to remove the enitre row: ").title()
    for row in myTodos:
      if choice in row:
        myTodos.remove(row)
    prettyPrint()    

  f = open("Event Planner", "w")    
  f.write(str(myTodos))
  f.close()


