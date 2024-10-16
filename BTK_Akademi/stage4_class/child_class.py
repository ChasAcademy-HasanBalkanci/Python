class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person class was created")
    def intro(self):
        print(self.name, self.surname, self.age)
    
class Student(Person):
    def __init__(self, name, surname, age, number):
        Person.__init__(self, name, surname, age)
        self.number = number
        print("Student class was created")
    def study(self):
        print(f"{self.name}, is studying.")
    

class Teacher(Person):
    def __init__(self, name, surname, age, department):
        Person.__init__(self,name, surname, age)
        self.department = department
        print("Teacher class was created")
    
    def teach(self):
        print(f"{self.name}, is teaching {self.department}.")
    
    def intro(self):
        print(self, self.name, self.surname, self.department)
    

 
# print("\nPerson Info: ")      
# p1 = Person("Hasan", "Balkanci", 41)
# p1.intro()

# print("\nStudent Info: ")
# s1 = Student("Cinar", "Turan", 7, 105)
# s1.intro()
# s1.study()
# print(s1.number)

print("\nTeacher Info: ")
t1 = Teacher("Ece", "Tuncel", 35, "Computer Science")
t1.intro()
t1.teach()
print(t1.department)
