# products = [{"title": "samsung s23", "price" : 70000"}, {"title": "samsung s24", "price" : 80000"}, {"title": "samsung s53", "price" : 90000"}]
products = [{"title": "samsung s23", "price" : 70000"}, 
            {"title": "samsung s24", "price" : 80000"}, 
            {"title": "samsung s53", "price" : 90000"}
]

max_price = max(products, key = lambda x: x["price"])
print(max_price)

total_price = sum([product["price"] for product in products])