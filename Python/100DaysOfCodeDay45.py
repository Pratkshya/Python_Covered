# Class Attendance Tracker

studentsList = {}

totalStudents = int(input("Enter the total number of students -> "))

for rollNo in range(1,totalStudents + 1):
  studentData = input("Enter the name of the students -> ")
  studentsList[rollNo] = {"name": studentData, "status":"A"}

while True:
  print("\n Current Attendance")

  for rollNo,detail in studentsList.items():
    print(f"{rollNo}. {detail['name']} - {detail['status']}")

  rollNo = int(input("\n Enter the roll number to update(0 to finish) -> "))  
  if rollNo == 0:
    break
  elif rollNo < 1 or rollNo > totalStudents:
    print("Invalid Roll No!!")
  elif rollNo in studentsList:
    studentsList[rollNo]["status"] = "p"
  else:
    print("Invalid roll number.")  

print("\n Final Attendance...")    
for rollNo,detail in studentsList.items():
  print(f"{rollNo}. {detail['name']} - {detail['status']}")


