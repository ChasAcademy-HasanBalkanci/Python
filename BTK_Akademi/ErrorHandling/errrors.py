# error
'''print(a) ==> NameError. Because a isnt defined.'''
'''int("1a2") ==> ValueError: invalid literal for int() with base 10: '1a2' ''' 
# print(10/0) ==> ZeroDivisionError: division by zero
# print('denem' e) ==> SyntaxError: invalid syntax. Perhaps you forgot a comma?


# error handling
'''
try:
    x = int(input('x : '))
    y = int(input('y : '))
    print(x/y)
#except ZeroDivisionError as e:
    #print("You should enter a number different from zero for 'y'.")

#except ValueError:
    #print("You should enter a valid number.")
except (ValueError, NameError, ZeroDivisionError) as e:
    print("You should enter a valid number for 'x' and a number different from zero for 'y'.")
    print(e)
'''
while True:
    try:
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)

    except Exception as ex:
        print("Having experienced an error!")
        print(ex)
    else:
        print("try except was executed")
        break
    finally:
        print("Finally block executed!")
