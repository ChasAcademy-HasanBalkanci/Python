"""def square(x):
    return x ** 2
"""

square = (lambda x : x ** 2 % 7) (11)
print(square)

plus = (lambda a, b, c : a + b + c)

result = plus(2, 3, 4)

print(result)