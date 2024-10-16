list_temp = [0, 10, 20, 30, 40]
list_fahr = list(map(lambda x: int(x * 9/5 + 32), list_temp))
print(f"The converted list contains the following : \n{list_fahr}")

# "Given a list of integers [1, 2, 3, 4, 5, 6, 7, 8, 9], 
# filter out the odd numbers and return a list where the even numbers are squared."
list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda x: x % 2 != 0, list_nums))
print(f"The odd number list : \n{odd_numbers}")

squared_even_numbers = [num ** 2 for num in list_nums if num %2 == 0]
print(f"The squared even number list : \n{squared_even_numbers}")

#"You have a list of dictionaries representing people:
# Write a function that returns the names of all people who are over 30 years old."
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 40}, {'name': 'Charlie', 'age': 30}]

over_30_years_old = [person["name"] for person in people if person["age"] > 30] 
print(over_30_years_old)

#"Given the sentence 'map and filter are useful functions',
# write a function that returns a list of the lengths of each word."
sentence = 'map and filter are useful functions'

word_lengths = [len(word) for word in sentence.split()]
print(word_lengths)

#"Given a list of numbers [-1, 4, -9, 16, 25], 
#filter out the negative numbers and return their square roots."
Numbers = [-1, 4, -9, 16, 25]
SquaredNegativNumbers = list(map(lambda x: x ** 2, [num for num in Numbers if num < 0]))
print(SquaredNegativNumbers)