# def exponential(number):

#     def inner(power):

#         return number ** power

#     return inner
# print(exponential(2)(3))
# def yetki_sorgula(page):

#     def inner(role):

#         if role == "admin":

#             return f"{role} rolüne sahip kisin sayfasına erişim sağlandı.", f"{page} sayfasına erişim sağlandı."

#         else:

#             return f"{page} sayfasına erişim reddedildi."

#     return inner
# user1 = yetki_sorgula("Product Owner")
# print(user1("admin"))

def calculation(calculate):
    def total(*args):
        toplama = 0
        for i in args:
            toplama += i
        return toplama

    def multiply(*args):
        result = 1
        for i in args:
            result *= i
        return result

    if calculate == "toplama":
        return total
    else:
        return multiply

islem = calculation("toplama")
print(islem(1,2,3,4,5))

    
            