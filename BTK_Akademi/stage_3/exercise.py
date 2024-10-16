# def square(num): return num ** 2

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# square_numbers = list(map(lambda num : num **2, list_numbers))
# print(square_numbers)

# square_root = list(map(lambda num : int(num ** 0.5), square_numbers))
# print(square_root)

# cube_root_funk = lambda num : ((num ** (1/3) ))

# # cube_root = list(map(cube_root_funk, list_numbers))

# #print(cube_root_)

# result = cube_root_funk(27)
# print(result)
# result_even = list(filter(lambda num : num % 2 == 0, list_numbers))
# print(result_even)
check_odd = lambda num : num % 2 == 1

result_odd = list(filter(check_odd, list_numbers))
print(result_odd)
result_odd = check_odd(9)
print(result_odd)