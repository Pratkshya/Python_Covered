import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date = datetime.date(year, month, day)
print(date)