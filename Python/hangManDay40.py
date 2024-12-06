import random,os,time

listOfWords = ["apple", "pear", "mango", "grapes"]
letterPicked = []
myWord = random.choice(listOfWords) #to select the random words
lives = 6

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()

  if letter in letterPicked:
    print("You've tried that before")
    continue

  letterPicked.append(letter)
  print()

  if letter in myWord:
   print("You've found a letter")
  else:
   print("Nope, not in there") 
   lives -= 1

  allletters = True
  print()
  for i in myWord:
    if i in letterPicked:
      print(i, end="") 
    else:
      print("_", end= "") 
      allletters = False
  print()   
  
  if allletters:
    print(f"You've won with {lives} left!")
    break

  if lives <= 0:
    print(f"You ran out of lives! The answer was {myWord}")
    break
  else:
    print(f"Only {lives} left!")
    print()
