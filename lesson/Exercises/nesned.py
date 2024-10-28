# def outer(num1):
#     print("outer")
#     def inner(num1):
#         print("inner")
#         return num1 +1
    
#     num2 = inner(num1)
#     print(num1, num2)

# outer(5)

# def factorial(num1):
#     if not isinstance(num1, int):
#         raise TypeError("num1 must be an integer")
#     if not num1 >= 0:
#         raise ValueError("num1 must be >= 0")
#     else:
#         return num1 + factorial(num1 -1)

# print(factorial(0))
# def usalma(num1):

#     def inner(power):
#         return num1 ** power
#     return inner

# print(usalma(2)(3)


def calculate_operation(operation_name):
    """Returns a function that performs the given calculation."""
    def sum_numbers(*args):
        """Returns the sum of the given numbers."""
        return sum(args)

    def multiply_numbers(*args):
        """Returns the product of the given numbers."""
        result = 1
        for num in args:
            result *= num
        return result

    operations = {
        "sum": sum_numbers,
        "multiply": multiply_numbers
    }

    return operations.get(operation_name, lambda *args: None)
result = calculate_operation("multiply")(2,3,4,5)
print(result)