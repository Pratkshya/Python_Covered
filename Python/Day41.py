#Use of .items()

myInfo = {"name": "Pratikshya", "age": 22,"education": "Bachelors"}

for keyValue, data in myInfo.items():
  print(f"{keyValue}: {data}")
  if (keyValue == "age"):
    print("You're in your 20s!")