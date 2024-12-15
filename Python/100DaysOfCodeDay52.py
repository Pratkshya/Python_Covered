import time,os
momoOrders = {}

try:
  f = open("Momo", "r")
  momoOrders = eval(f.read())
  f.close()
except:
  print("ERROR. Unable to load content")  

def view():
  print()
  print("MOMOSss")
  print("\n{:^15} {:^15} {:^15} {:^15} {:^15}".format("Name", "Type", "Size", "Quantity", "Total"))  # Centered Header
  print("-" * 90)

  for name, value in momoOrders.items():
    print(f"{name:^15} {value['type']:^15} {value['size']:^15} {value['quantity']:^15} {value['total']:^15}")
    print()  

def totalAmt():
  h = 60
  f = 120
  if size == "h":
    totalAmount = h * quantity
    return totalAmount
  elif size == "f":
    totalAmount = f * quantity
    return totalAmount
  
while True:

  print("\nPratkshyas MOMOS\n")
  menu = int(input("1.Add momo\n2.View order placement\n> "))
  if menu == 1:
    print()
    name = input("Name: ")
    type = input("MOMO: ")

    while True:
        size = input("Size[h/f]: ").lower()
        if size in ['h','f']:
         break
        else:
          print("Enter either h/f i.e. half plate or full plate as mentioned!")

    while True:
      #Exits if integer
      try:
        quantity = int(input("Quantity: "))
        break
      #Raises error
      except ValueError:
        print("Invalid input. Enter interger number for quantity")
    total = totalAmt() 
    momoOrders[name] = {"type": type,"size": size, "quantity": quantity, "total": total}
    print("\nYour order was placed\n")
    time.sleep(1)
    os.system("clear")

  elif menu == 2:
      view()
  else:
    print("Please select from the displayed number.")

  f = open("Momo", "w")  
  f.write(str(momoOrders))
  f.close()
    