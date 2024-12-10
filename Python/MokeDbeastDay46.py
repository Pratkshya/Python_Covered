
mokeBeast = {}
def prettyPrint():
  print(f"Name\tType\tHP\tMP")
  for key,value in mokeBeast.items():
    print(f"""{key:^8}|{value["type"]:^8}|{value["Hp"]:^4}|{value["Mp"]:^4}""")
    print()  
  print()  
while True:
  print("\nMokeBeasts Full-on MokeDex\n")
  user = print("Your build: ")
  name = input("Name > ")
  type = input("Type > ")
  Hp = int(input("HP > "))
  Mp = int(input("MP > "))
  
  mokeBeast[name]= {"type": type, "Hp": Hp, "Mp": Mp}
  print()
  print("------------------")
  prettyPrint()
