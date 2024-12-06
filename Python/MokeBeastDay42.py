mokeBeast  = {"Beast Name":None, "Type":None, "Special Move":None,"HP":None, "MP":None}

print("!MokeBeast!")
print()
for name,value in mokeBeast.items()  :
  mokeBeast[name] = input(f"{name} : ").strip().upper()

if mokeBeast["Type"] == "FIRE" :
  print("\033[31m", end="")
elif mokeBeast["Type"] == "EARTH" :
  print("\033[32m", end="")
elif mokeBeast["Type"] == "WATER" :
  print("\033[36m", end="")
elif mokeBeast["Type"] == "LAND" :
  print("\033[33m", end="")
else:
  print("\033[35m", end="")

for name,value in mokeBeast.items()  :
  print()
  print(f"{name:<12} : {value}")