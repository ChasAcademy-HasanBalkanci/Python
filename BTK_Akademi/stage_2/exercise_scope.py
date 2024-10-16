
# name = "global string"
# def greating():
#     name  = "Cinar"
#     def hello():
#         print("Hello " + name)
#     hello()
# greating()

x = 50
def test():
    global x  # to modify global variable
    print(f"Test : {x}" )
    x = 100
    print("Test :" + str(x))
test()
print(f"Global scope : {x}")