class Person:
    def __init__(self, name, year):
            
        if len(name) > 10:
            raise ValueError("Name should not exceed 10 characters")
        else:
            self.name = name
        if year > 2024:
            raise ValueError("Year should not be in the future")
        else:
            self.year = year

p = Person("Alieeeeeeeeee", 19897)

print(p.name)