import datetime

print("\nEVENT COUNTDOWN")
print("-" * 15)

today = datetime.date.today()

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
event = datetime.date(year, month, day)

difference = event - today
difference = difference.days

if difference > 0:
  print(f"😄😄😄😄 {difference} days to go")
elif difference < 0:
  print(f"🥲🥲🥲🥲 Missed by {difference} days")  
else:
  print("🥳🥳🥳🥳 Today")  
