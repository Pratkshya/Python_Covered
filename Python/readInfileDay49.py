f = open("high.score", "r")
gameContents = f.read().split("\n")
f.close()
highscore = 0
for rows in gameContents:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print(f"The winner is", name, "with", highscore)

   



