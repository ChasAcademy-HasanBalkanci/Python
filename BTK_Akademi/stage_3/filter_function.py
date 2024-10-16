numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, 0, -2, -3, -4, -5, -6, -7]
result_negativ = list(filter(lambda x: x <0, numbers))
print(result_negativ)
result_even = list(filter(lambda x : x % 2 == 0, numbers))
print(result_even)
result_negativ_odd = list(filter(lambda x : x % 2 != 0 and x < 1, numbers))
print(result_negativ_odd)

names = ["Hasan", "Felix", "Jhonas", "Martin", "matalie"]
result_names = list(filter(lambda x: len(x) > 5 and x[0].lower() != "m", names))
print(result_names)