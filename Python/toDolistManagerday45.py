"""TO DO LIST MANAGER"""
import os,time
print("\nTO DO LIST MANAGER\n")
toDolist = []
  
def add():
        os.system("clear")
        time.sleep(1)
        name = input("Todo for a day -> ").title()
        day = input("Due -> ")
        priority = input("Set priority(high/medium/low) -> ").capitalize()
        row = [name,day,priority]
        toDolist.append(row)
        print("ADDED")
def view() :
        os.system("clear")
        time.sleep(1)
        options = int(input("\n1. All\n2. By priority\n-> "))
        if options == 1:
                for row in toDolist:
                        for item in row:
                                print(f"{item}", end = " | ")
                        print()
                print()                
        elif options == 2:
                priority = input("Enter by priority -> ").capitalize()
                for row in toDolist:
                        if priority in row:
                                for item in row:
                                        print(f"{item}", end = " | ")
                                print()        
                print()    

def edit() :
        os.system("clear")
        time.sleep(1)
        find = input("Name of todo to edit -> ")
        found = False
        for row in toDolist:
                if find in row:
                        found = True
        if not found:
                print("Couldn't find in the list...")                
                return
        for row in toDolist:
                if find in row:
                        toDolist.remove(row)
        name = input("Todo for a day -> ").title()
        day = input("Due -> ")
        priority = input("Set priority(high/medium/low) -> ").capitalize()
        row = [name,day,priority]
        toDolist.append(row)
        print("ADDED")

def remove() :
        os.system("clear")
        time.sleep(1)
        find = input("Name of todo to remove -> ")
        for row in toDolist:
                if find in row:
                        toDolist.remove(row)
     
while True:
        choice = int(input("\n1. Add\n\n2. View\n\n3. Edit\n\n4. Remove\n-> "))
        if choice == 1:
                add()
        elif choice == 2:
               view()
        elif choice == 3:
               edit()       
        elif choice == 4:
               remove()
        time.sleep(1)
        os.system("clear")