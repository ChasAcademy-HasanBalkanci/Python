# x, y = 1, 2
# x = y
# y = 6
# print(x)
# print( x == y)
# print( x is y)

# total_odd = sum([num for num in range(1, 101, 2) ])
# print(total_odd)

# text = "Hasan"
# willing_index = input("Please write the letter you want to know its index : ").lower()
# counter = 0
# for i in text.lower():
    
#     if i == willing_index:
#         print(f"The letter '{willing_index}' is found at index {counter}.")
#         break
    
#     counter += 1

#
import random

# def GenerateNumber():
#     return random.randint(1, 100)

# gen_number = GenerateNumber()

# guess_number = int(input("Please enter a number to guess: "))
# list_guess_number = []


# while guess_number!= gen_number:
#     if guess_number < gen_number:
#         print("Too low. Try again!")
#     elif guess_number == gen_number:
#         print("Congratulations! You guessed the number correctly.")
#         break
#     else:
#         print("Too high. Try again!")
#     list_guess_number.append(guess_number)
#     print(f"Your guessed numbers are : {list_guess_number}")
#     guess_number = int(input("Please enter a number to guess: "))

number = int(input("Please enter a number to check if it is prime : "))

                   
check_prime_lsit = bool([num for num in range(2, number)  if number % num == 0])

if check_prime_lsit == False:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")