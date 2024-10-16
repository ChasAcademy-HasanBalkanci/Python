class Person:
    # atribute class attribute
    adress = "no information available"
    # methods
    # constructor attributes
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("init mod was run")


p1 = Person("Hasan", 1983)
print(f"{p1.name} was born in {p1.year} ")
