import csv
with open("products.csv") as file:
    csv_reader = csv.reader(file)
    # list_reader = list(reader)
    # print(list_reader[0])
    #next(csv_reader)


    next(csv_reader)
    for row in csv_reader:
        #print(i[3])
        if row[3] == True:
            print(row)
    