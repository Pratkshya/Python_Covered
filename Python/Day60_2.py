import datetime

today = datetime.date.today()

mydate = datetime.date(year = 2025, month = 1, day = 1)

if today < mydate:
  print("Still more to go")
elif today > mydate:
  print("You missed it")
else:
  print("It's tiiiimeee")
  
