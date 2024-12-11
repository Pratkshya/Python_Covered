import time,os,random
while True:
  os.system("clear")
  time.sleep(1)
  print("\nIDEAS\n")
  menu = int(input("1. Add an idea\n2. Load up a random idea\n> "))
  if menu == 1:
    print()
    print("IDEAS\n")
    idea = input("Idea > ")

    f = open("Idea Storage", "a+")
    f.write(f"{idea}\n")
    f.close()

    print("\nADDED")
    time.sleep(1)
    os.system("clear")

  elif menu == 2:
     os.system("clear")
     time.sleep(1)

     f = open("Idea Storage", "r")
     loadUp = f.readlines()
     f.close()
     
     if not loadUp:
       print("No ideas availabe! Add some first")
     else:
       randomChoice = random.choice(loadUp).strip()
       print(f"Random Idea: {randomChoice}")
    
     time.sleep(1)
     os.system("clear")



