#BINGO GAME

import random,os,time

print()
print("Bingo Game Generator...")
print()

def rand():
 randNum = random.randint(1,90)
 return randNum

def prettyPrint():
 for row in bingoNum:
   for item in row:
    print(item, end="  |  ")
   print()  

def check():
  global bingoNum
  generatedNum = []
  for i in range(8):
    num = rand()
    while num in generatedNum:
      num = rand()
    generatedNum.append(rand())
    
  generatedNum.sort() 

  bingoNum = [[generatedNum[0],generatedNum[1],generatedNum[2]],
              [generatedNum[3],"BG",generatedNum[4]],
              [generatedNum[5],generatedNum[6],generatedNum[7]]] 

check()
while True:
  prettyPrint()
  num = int(input("Next number -> "))
  for row in range(3):
    for item in range(3):
      if bingoNum[row][item] == num:
        bingoNum[row][item] = "X"

  exes = 0
  for row in  bingoNum:
    for item in row:
      if item == "X":
        exes += 1

  if exes == 8:
    print("You WON")
    break

  time.sleep(1)
  os.system("clear")
