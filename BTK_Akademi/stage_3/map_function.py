# def squares(number):
#     return number * number (Ctrl + K + C)

# def square(number):
#     return number ** 2

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square = map(lambda x : x ** 2, list_of_numbers) # The result stores on memory. We need to list the map functions.
print(list(square))

list_of_strings = [ "1", "2", "3", "4"]
list_of_strings_1 = [ "1", "2", "3", "4", "a", "b", "c", "d", "e"]

number_of_strings = list(map(int, list_of_strings))

number_of_strings_1_new = [item for item in list_of_strings_1 if item.isdigit()]
number_of_strings_1 = list(map(lambda x : int(x), number_of_strings_1_new ))

print(number_of_strings)

print(number_of_strings_1)