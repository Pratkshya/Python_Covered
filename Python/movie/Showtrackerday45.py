import os, time
movieList = []

def add():
      # os.system("clear")
      # time.sleep(1)
      title = input("Enter the title: ").title()
      genre = input("Enter the genre: ")
      status = input("Enter the status (Watcehd/To Watch): ")
      movie = {"title":title, "genre":genre,"status":status}
      movieList.append(movie)
      print("\nAdded to the list...\n")

def view():
      # os.system("clear")
      # time.sleep(1)
      if not movieList:
            print("\nNo movies/shows in the list\n")
            input("Press enter to continue...")

      else:      
          start = 1
          for movie in movieList:
                print(f"{start}. {movie['title']} | {movie['genre']} | {movie['status']}")
                start += 1
          input("Press enter to continue...")
          print()  

def remove() :
      find = input("Enter the title of movie/show you want to remove -> ")
      found = False
      for movie in movieList:
            if movie['title'].title() == find.title():
                  movieList.remove(movie)
                  found = True
                  print(f"Removed {find} from the list.")
                  break
      if not found:
            print("No such movise/show found.")      
      input("Press enter to exit...\n")

def edit():
      new = input("Enter the name of the movie/show you want to edit -> ").title()
      found = False
      for movie in movieList:
            if movie['title'].title() == new:
                  found = True
                  title = input("Enter the new title: ").title()
                  genre = input("Enter the new genre: ")
                  status = input("Enter the new status (Watcehd/To Watch): ")
                  print(f"\n '{new}' has been updated successfully.\n")
                  break
      if not found:
            print("\nNo such movie/show...\n")      
      input("Press enter to continue...")            

def exit():
       print("\nThank you for using the Movie/TV Show Tracker. Goodbye!\n")
       input("Press Enter to exit...")
       os.system("clear")

while True:
      # os.system("clear")
      # time.sleep(1)
      print("\n--- Movie/TV Show Tracker ---")
      menu = int(input("\n1. Add a Movie\Show\n2. View All Movies/Shows\n3. Edit an Entry\n4. Remove an Entry\n5. Exit\n\n-> "))
      if menu == 1:
            add()
      elif menu == 2:
            view()  
      elif menu == 3:
            edit()          
      elif menu == 4:
            remove()      
      elif menu == 5:
            exit()      