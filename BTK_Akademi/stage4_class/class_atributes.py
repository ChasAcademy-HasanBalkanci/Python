class CarItem:
    discount_rate = 0.8
    item_count = 0
    # constructor
    def __init__(self, name, price, quantity):
        # instance properties, attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        CarItem.item_count += 1
    
    # instance methods¨
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price *= (1 - CarItem.discount_rate)


# instance
item1 = CarItem("Telefone", 70000, 500)
item2 = CarItem("Computer", 65000, 300)
item3 = CarItem("Book", 300, 900)

print(CarItem.item_count)  # 3

item1.apply_discount()
print(item1.calculate_total())

item2.apply_discount()
print(item2.calculate_total())

item3.apply_discount()
print(item3.calculate_total())