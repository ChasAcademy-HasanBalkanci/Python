# Generators : A generator is a function that returns an iterator that not be stored in memory.

from unittest import result


# def cube():
#     result = []
#     result = [i ** 3 for i in range(5)]
#     return result

# result = cube()
# print(result)

# def square():
#     for i in range(500):
#         yield i ** 2

# result = square()
# #iterator = iter(result)
# while True:
#     try:
#         print(next(result))
#     except StopIteration:
#         break
liste_1 = [num ** 3 for num in range(1, 11, 2)]
print(liste_1)
liste_2 = (num ** 3 for num in range(1, 11, 2))
while True:
    try:
        print(next(liste_2))
    except StopIteration:
        break