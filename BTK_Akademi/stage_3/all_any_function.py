numbers = [2,  4, 6, -8]
# check all number is grater than 0

result = all([bool(number) for number in numbers])
print(result)

all_even = all([number % 2 == 0 for number in numbers])
print(all_even)