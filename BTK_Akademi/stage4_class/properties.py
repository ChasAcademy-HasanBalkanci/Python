class Product:
    def __init__(self, name, price):
        self.name = name
        if price > 0:
            self._price = price
        else:
            raise ValueError("It's not allowed to assign negativ price!")
    @property   
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("It's not allowed to assign negativ price!")

    
    # def set_price(self, value):
    #     if value >= 0:
    #         self._price = value
    #     else:
    #         raise ValueError("It's not allowed to assign negativ price!")
    
    # def get_price(self):
    #     return self._price

        


p = Product("Iphone", 80000)
p.price = 300
print(p.price)
#p.price(70000)
# print(p.get_price())
# p.price = -70000
#print(p.name, p.price)    