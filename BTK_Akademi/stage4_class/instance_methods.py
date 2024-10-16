class CarItem:
    # constructor
    def __init__(self, name, price, quantity):
        # instance properties, attributes
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # instance methods¨
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self, rate):
        self.price *= (1-rate)


# instance
item1 = CarItem("Telefone", 70000, 500)
item2 = CarItem("Computer", 65000, 300)
item3 = CarItem("Book", 300, 900)

item1.apply_discount(0.9)
print(item1.calculate_total())
print(item2.calculate_total())
print(item3.calculate_total())
