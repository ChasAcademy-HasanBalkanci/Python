class CarItem:
    discount_rate = 0.8
    item_count = 0
    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} products were procuded."
    @classmethod
    def create_item(cls, data_str):
        name, price, quantity = data_str.split(",")
        return cls(name, float(price), int(quantity))
  
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CarItem.item_count += 1
    def calculate_total(self):
        return self.price * self.quantity    
    def apply_discount(self):
        self.price *= (1 - CarItem.discount_rate)

print(CarItem.display_item_count())
item1 = CarItem("Telefone", 70000, 500)
item2 = CarItem("Computer", 65000, 300)
print(item1.display_item_count())
item3 = CarItem("Book", 300, 900)
item4 = CarItem("Book", 3, 8)

CarItem.create_item("Mouse, 800, 3")
print(CarItem.display_item_count())

