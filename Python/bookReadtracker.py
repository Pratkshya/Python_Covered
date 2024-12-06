#Book Read Tracker

book = {}
print("\nBook Read Tracker...\n")
bookNo = int(input("How many books you want to read this year? -> "))

for num in range(1,bookNo + 1):
    bookName = input("Enter Book Name -> ").strip().title()
    book[num]  = {"name": bookName, "status": "In Queue"}

while True:
    print("\n Current Book List To Read...")
    for num,detail in book.items():
        print(f"{num}. {detail['name']} - {detail['status']}")
    
    print("\nEdit the Book you've read:")
    print()
    num = int(input("Number the books you've read or press 0 to exit -> "))
    if num == 0:
        break
    elif num < 1 or num > bookNo:
        print("Invalid Number!!!")
    elif num in book:
      book[num]['status'] = "Read" 

print("\nUpdated Book Read Tracker\n")  
for num,detail in book.items():
    print(f"{num}. {detail['name']} - {detail['status']}")
