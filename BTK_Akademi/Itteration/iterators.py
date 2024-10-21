liste = [1, 2, 3, 4, 5]

iterator = iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(dir(liste))

# for i in liste:
#     print(i)

# from operator import truediv


# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            result = self.start
            self.start += 1
            return result
        else:
            raise StopIteration
list = MyNumbers(1, 10)

my_iter = iter(list)
print(next(my_iter))
