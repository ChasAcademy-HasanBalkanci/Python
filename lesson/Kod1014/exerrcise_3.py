def find_prime_number(firstnumber, secondnumber):
    """
    This function finds all prime numbers between the given two numbers.
    """
    prime_list = []
    for num in range(firstnumber, secondnumber + 1):
        for i in range(2, num ):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    
    print(prime_list)
 

find_prime_number(3, 90)