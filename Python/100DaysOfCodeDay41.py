myDictionary = {"Name": None, "url": None, "description": None, "rating": None}

for name, value in myDictionary.items():
  myDictionary[name] = input(f"{name}: ")

print()  

for name, value in myDictionary.items():
  print(f"{name}: {value}")


  
