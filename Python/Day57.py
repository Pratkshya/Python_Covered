#Recursion

def reverse(value):
  if value <= 0:
    print("Completed pattern")
    return
  else:
    for i in range(value):
      print("🌸", end = "")  
    print()
    reverse(value - 1)
  
reverse(10)