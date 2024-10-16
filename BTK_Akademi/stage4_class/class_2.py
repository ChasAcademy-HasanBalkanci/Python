class Person:

    adress = "Adres is not available!"

    def __init__(self, name, year):
        self.name = name
        self.year = year


    def intro(self):
        print(f"Hello there! My name is {self.name}")
    
    def calculateAge(self):
        age = 2024 - self.year
        return age


p1 = Person(name = "Hasan", year = 1983)
p1.intro()
print(p1.calculateAge())

class Circle:
    # ckass object atribute
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def calculateCircumference(self):
        return 2 * self.pi * self.radius
    
    def calculateArea(self):
        return self.pi * self.radius ** 2

c1 = Circle(radius = 5)
print(f"Area is {c1.calculateArea()}. Circle is {c1.calculateCircumference()}")
