#JOB DETAILS

class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked
    
  def display(self):
    print("\nJOBS")
    print("-" * 6)
    print(f"""{self.name:<15} {self.salary:^10} {self.hoursWorked:>15}""" )

class doctor(job):

  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def display(self):
    print("\nJOBS")
    print("-" * 6)
    print(f"""{self.name:<15} {self.salary:^10} {self.hoursWorked:>15}""" )
    print(f"{self.experience:<10} {self.speciality:>12}")  

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.subject = subject
    self.position = position
    
  def display(self):
    print("\nJOBS")
    print("-" * 6)
    print(f"""{self.name:<15} {self.salary:^10} {self.hoursWorked:>15}""" )
    print(f"{self.subject:<10} {self.position:>20}")  
  


lawyer = job("Laywer", "$100,000", "40")
lawyer.display()

doc = doctor("$230,000", "47", "6", "Neuro")
doc.display()

tech = teacher("$60,000", "48+", "CompSci", "Vice.Principle")
tech.display()