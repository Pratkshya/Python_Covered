vowels = ["a", "e", "i", "o","u"]

askUser = input("Type something > ")
for letter in askUser:
  if letter.lower() in vowels:
   print('\033[33m', end='')
  print(letter, end='')
  print('\033[0m', end='')
  print( )