#Factorial Sum
import time,os
def factorial(value):
  if value == 1:
    return 1
  elif value <= 0:
    print("Terminated")
  else:
      time.sleep(1)
      os.system("clear")
      print("Calculating sum...")
      return value + factorial(value - 1)

time.sleep(1)
print(f"The factorial sum is: {factorial(4)}")  