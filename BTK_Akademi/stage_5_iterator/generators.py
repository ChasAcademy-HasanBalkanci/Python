# (1- infinity) between this space, produce a funktion that comes out the square of the number.

def produce_number():
    num = 0
    while True:
        yield (num) ** 2
        num += 1
generator = produce_number()
print(next(generator))
print(next(generator))
print(next(generator))

# Create fibonacci both normal methot and using generator funktion.

def fib_list(max):
    numbers = []
    a, b = 0, 1
    while len(numbers) < max:
        numbers.append(a)
        a, b = b, a+b
    return numbers
print(fib_list(5))

def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count < max:
        yield a
        a, b = b, a+b
        count += 1
    return a
for i in fib_gen(max):
    print(i)
