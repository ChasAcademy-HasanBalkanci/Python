from gzip import FNAME


class Personal():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

        print("Personal class run")
    def who_am_I(self):
        print("I am a person")
    def eat(self):
        print("I eat")

class Student(Personal):
    def __init__(self,fName, lName, email, number):
        Personal.__init__(self, fName, lName )
        self.email = email
        self.number = number
        print("Student class run")
        print(f"Name : {self.fName}, Last Name : {self.lName}, Email : {self.email}")
    
    def who_am_I(self):
        print("I am a student")

class Teacher(Personal):
    def __init__(self, fName, lName, department):
        Personal.__init__(self, fName, lName)
        self.department = department
        print("Teacher class run")
        print(f"Name : {self.fName}, Last Name : {self.lName}, Department : {self.department}")

    def who_am_I(self):
        print("I am a teacher")

        
p1 = Personal("Ali", "veli")

s1 = Student("Ali", "Hasan", "as@gmail.com", 1205)

p1.who_am_I()
s1.who_am_I()
