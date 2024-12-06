print("Anonymous Name Generator")
print()
firstName = input("Your First Name: ").strip()
lastName = input("Your last Name: ").strip()
city = input("City you were born in: ").strip()
pet = input("Your favourite pet: ").strip()

nameGenerator = f"{firstName[:2].capitalize()}{lastName[:3].lower()} {city[:3].title()}{pet[:-2]}"
print(f"Your Anonymous Name is: {nameGenerator}")

