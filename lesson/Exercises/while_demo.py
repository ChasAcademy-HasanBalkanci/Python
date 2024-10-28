# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counter = 0
# while counter < len(numbers):
#     print(numbers[counter])
#     counter += 1

# begining, ending= int(input("Enter the beginning of numbers: ")), int(input("Enter the end of numbers: "))
# even_number = [num for num in range(begining, ending + 1) if num % 2 != 0]
# print (even_number)

# for i in range(100, 0, -1):
#     print(i)
# list_number = []
# counter = 0
# while True:
#     if counter == 5:
#         break
#     num = int(input("Enter a number: "))
#     counter += 1
#     list_number.append(num)
# list_number = sorted(list_number)
# print(list_number)
# myString = "Python is a programming language"
# x = myString.upper()
# print(myString)
# print(x)

# def sayHello(user = "Guest"):
    # return f"Hello {user}!"
# msg = sayHello("John")
# print(msg)
# def total(num1, num2 = 1):
    # result = num1 + num2
    # return result

# def squre(num1, num2= total(5, 0)):
#     result = num1 ** num2
    
#     return result
# # print(squre(2))
# word = input("Enter a word: ")
# word = word +  "\n"
# times = int(input("How many times to repeat: "))
# def write_word(word, times):
#     print(word * times)

# write_word(word, times)

# def make_list(*args):
#     return [*args]

# print(make_list(1, 2, 3, 4, 5))

# def find_prime(num1: int = 1, num2: int = 1) -> None:
#     """
#     Finds and prints all prime numbers between num1 and num2.

#     This function will find all prime numbers in the range from num1 to num2 and print them out.
#     A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#     The range is inclusive of both num1 and num2.

#     Args:
#         num1 (int): The start of the range (inclusive). Defaults to 1.
#         num2 (int): The end of the range (inclusive). Defaults to 1.
#     """
#     # Create an empty list to store the prime numbers.
#     prime_numbers = []
    
#     # Loop through all numbers in the range from num1 to num2.
#     for num in range(max(num1, 2), num2 + 1):
#         # Assume the current number is prime until proven otherwise.
#         is_prime = True
        
#         # Loop through all numbers from 2 to the square root of num.
#         for x in range(2, int(num**0.5) + 1):
#             # If num is divisible by x, then it's not a prime number.
#             if num % x == 0:
#                 is_prime = False
#                 break
        
#         # If the number is prime, add it to the list of prime numbers.
#         if is_prime:
#             print(num)
# print(find_prime())

#find prime dividers of a number: For exempel 45 ==> [1, 3, 5 ]
# def find_prime_divisors(number):
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True

#     prime_divisors = []
#     for i in range(1, number + 1):
#         if number % i == 0 and is_prime(i):
#             prime_divisors.append(i)
#     return prime_divisors

# number = 363
# print(find_prime_divisors(number))  # Output: [3, 5]


# num = int(input("Enter a number: "))
# def find_prime_dividers(num):
#     dividers = []
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     for i in range(1, num + 1):
#         if num % i == 0:
#             dividers.append(i)
#     return dividers

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# filtered_list = list(filter(lambda x : x % 2 == 0, num_list))
# func_square = lambda x : x ** 2
# x = map(func_square, filtered_list)

# print(list(x))













