class Bill:
    def __init__(self, name, model, colour):
        self.name = name
        self.model = model
        self.colour = colour

    def __str__(self):
        return f"Bill: {self.name} - {self.model}, Colour: {self.colour}"
my_bill = Bill("Volvo", "S40", 20000)
print(my_bill)

class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Punkt(1, 2)
p2 = Punkt(2, 3)
p3 = Punkt(2, 3)
print(p1 == p2)
print(p2 == p3)