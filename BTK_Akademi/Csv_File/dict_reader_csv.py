import csv
with open("products.csv") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        if row["Category"] == "Electronics":
            print(f"{row['Product Name']} costs {row['Price']}")