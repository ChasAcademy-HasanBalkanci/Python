# funktion is an object
# def greeting(name):
#     print(f"Hello {name}")

# greeting("Cinar")
# print(greeting("Hasan"))
# print(greeting)
# encapsulation
# def outer(num1):
#     print("outer")
#     def inner(num1):
#         print("inner")
#         return num1 +1
#     num2 = inner(num1)
#     print(num1, num2)
# outer(5)   
    
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))