# 2D dictionaries

mydict = {}
def prettyPrint():
  print()
  for key,value in mydict.items():
    print(key, end= ": ")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end = " | ")
    print()  

while True:
  name = input("Name : ")
  lName = input("Last Name : ")
  rollNo = input("Roll no : ")
  faculty = input("Faculty : ")

  mydict[name] = {"last Name ->" : lName, "rollNo ->" : rollNo, "faculty ->" : faculty}
  prettyPrint()  