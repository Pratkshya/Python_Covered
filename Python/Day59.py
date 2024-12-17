#Palindrome - it is a word which is same front and back.
import os,time
def palindrome(word):
  if word == "":
    print("Please enter a word to check")  
  elif word == word[::-1] :
    print(f"The given word {word} is a Palindrome")
    time.sleep(1)
  else:
    print(f"The word {word} is not  a Palindrome")  

while True:
  time.sleep(1)
  os.system("clear")
  print("\nPalindrome Checker")
  print("-" * 20)
  word = input("Give me a word: ").lower()
  #Function call
  palindrome(word)
