def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(1,2))
    elif islem_adi == "cikarma":
        print(f2(1,2))
    elif islem_adi == "carpma":
        print(f3(1,2))
    elif islem_adi == "bolme":
        print(f4(1,2))
    
    else:
        print("Hatalı islem adı girdiniz")

islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "cikarma")