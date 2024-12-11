import time,os

while True:
  os.system("clear")
  time.sleep(1)
  print("HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ")
  score = int(input("SCORE > "))
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  
  print("ADDED")
  time.sleep(1)
  os.system("clear")
