# def sub_multible():
#     liste_sub_multible = []
#     number = int(input('Write a number you want to know its sub multibles : '))
    
#     for i in range(1, number + 1):
#         if number % i == 0:
            
           
#             liste_sub_multible.append(i)

#     print(liste_sub_multible)

# sub_multible()

def sub_multible():
    liste_sub_multible = []
    number = int(input('Write a number you want to know its sub multibles : '))
    
    for i in range(2, number + 1):
        if number % i == 0:           
           liste_sub_multible.append(i)
           number /= i
           print(number)

    print(liste_sub_multible)

sub_multible()