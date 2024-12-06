import time, os,random
print()
print("...Typing Speed Game...")
print()
print("Are you ready to begin?")

listOfWords = ["asthetic", "decorative", "anonymous"]
print("Press enter to continue...")
input("")

wordsTyped = []
totalWords = 3
lives = 6
correctWords = 0
totalTime = 0


while True:
 if correctWords >= totalWords:
  print("Congratulations! You've completed the typing game.")
  break
 if lives <= 0:
  print("Game over! You've ran out of lives.")  
  break
 os.system("clear")

 words = random.choice([w for w in listOfWords if w not in wordsTyped])
 print(f"Your word is: {words}\n")
 startTime = time.time()
 type = input("> ").strip()
 endTime = time.time()

 timeTaken = endTime - startTime

 if type == words:
  print(f"Correct! You took {timeTaken:.2f} seconds.")
  wordsTyped.append(words)
  correctWords += 1
  totalTime += timeTaken
 else:
  print("That's incorrect. Try again.")
  lives -= 1

 time.sleep(1)  

os.system("clear") 
print("Game Over!")
print(f"You typed {totalWords} out of {correctWords} words correctly")
if correctWords > 0:
 print(f"Your average time per word was {totalTime / correctWords:.2f} seconds.")
else:
 print("Try practicing to improve your accuracy and speed.")
 print(f"Remaining lives: {lives}")