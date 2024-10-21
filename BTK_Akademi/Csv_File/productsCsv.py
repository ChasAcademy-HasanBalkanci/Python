import csv
import random

# Define the categories and ratings
categories = ["Electronics", "Fashion", "Home Goods", "Sports", "Toys"]
ratings = [1, 2, 3, 4, 5]

# Define the product names
product_names = [
    "Apple Watch",
    "Nike Shoes",
    "Samsung TV",
    "Adidas Shirt",
    "Sony Headphones",
    "LG Fridge",
    "Canon Camera",
    "HP Laptop",
    "Dell Monitor",
    "Microsoft Xbox",
    "PlayStation Console",
    "Nintendo Switch",
    "FIFA Soccer Ball",
    "Nike Basketball",
    "Under Armour Socks"
]

# Create the CSV file
with open("products.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Id", "Product Name", "Price", "IsActive", "Category", "Rating"])

    # Write the product rows
    for i in range(15):
        product_name = random.choice(product_names)
        price = round(random.uniform(10.0, 100.0), 2)
        is_active = random.choice([True, False])
        category = random.choice(categories)
        rating = random.choice(ratings)

        writer.writerow([
            i + 1,
            product_name,
            price,
            True if is_active else False,
            category,
            rating
        ])