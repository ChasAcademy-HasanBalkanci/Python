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


item1 = CarItem("Telefone", 70000, 500)
item2 = CarItem("Computer", 65000, 300)
item3 = CarItem("Book", 300, 900)

class ShoppingCart:
    def __init__(self, list_of_items):
        self.list_of_items = list_of_items

        def add_item(self, item):
            self.list_of_items.append(item)
            
        def display_items(self):
            for item in self.list_of_items:
                print(f"Name: {item.name}, Price: {item.price}")
        def calculate_totals(self):
            return sum([item.calculate_total() for item in self.list_of_items])  
        def remove_items(self, cart_item):
            self.list_of_items  = [item for item in self.list_of_items if item != cart_item] 
        def clear(self):
            self.list_of_items = []   

sc = ShoppingCart([item1, item2])
sc.add_item(item3)
sc.display_items()

# print(sc.calculate_totals())
# sc.remove_items(item1)
# sc.display_items()
# sc.clear()