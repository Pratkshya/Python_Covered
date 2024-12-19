#Concept of OOP

class school:
  name = None
  noOfstudents = None
  established = None

  def __init__(self, name,noOfstudents, established):
    self.name = name
    self.noOfstudents = noOfstudents
    self.established = established

  def allSchool(self):
    print(f"{self.name} was established in {self.established}")

class gvtSchool(school):
  language = None

  def __init__(self,language):
    self.name = "Jyoti School"
    self.established = "1967"
    self.language = language

school1 = school("Peace Zone", "1200", "1998")  
school1.allSchool() 

school2 = school("Garden Academy", "580", "2001")  
school2.allSchool()  

school3 = gvtSchool("Nepali")
school3.allSchool()
print(school3.language)