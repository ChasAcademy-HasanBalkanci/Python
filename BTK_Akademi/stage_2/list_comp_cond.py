
# List comprehension to generate a list of numbers from 1 to 100 that are divisible by 12
list_12 = [item for item in range(1, 101) if item % 12 == 0]
print (list_12)

text = "Hello 12345 World!"	
list_number = [int(item) for item in text if item.isdigit()]

print(list_number)

temprature = [20, 22, -3, -2, -1, 0, "Hello"]

# Using list comprehension to filter out temperatures below 0

filtered_temp = [temp if type(temp) == int and temp >= 0 else "icing hazard" for temp in temprature ]
print(filtered_temp)

students = ["Ali", "Canan", "Ahmet"]
degrees = [60, 50, 90]

# Using list comprehension to create a dictionary with students as keys and their corresponding degrees as values

student_degrees = {student : degree for student, degree in zip(students, degrees)}
print(student_degrees)

# Using list comprehension to calculate the sum of squares of the first 100 natural numbers
result = [(item_1, item_2) for item_1 in range(3) for item_2 in range(3)]

print(result)