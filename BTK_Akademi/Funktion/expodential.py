def exponential(base):
    def inner(power):
        return base **power
    return inner
def getInfo():
    base = int(input("Enter the base: "))
    power = int(input("Enter the power: "))
    if base == 0 and power == 0:
        print("The result is 1")
    
    elif base == 0 and power >= 1:
        print("The result is 1")
    else:
        print("The result is", exponential(base)(power))
    

getInfo()
    