


def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b    

def carpma(a, b):    
    return a * b    

def bolme(a, b):
    return a / b

islem_adi = input("İslem adını giriniz: \n1.1. Toplama\n1.2. Çıkarma\n1.3. Çarpma\n1.4. Bölme\n")

def islem(toplama, cikarma, carpma, bolme, islem_adi):
    
    if islem_adi == "toplama":
        a = int(input ("a: "))
        b = int(input ("b: "))
        print(toplama(a,b)) 
    elif islem_adi == "cikarma":
        a = int(input ("a: "))
        b = int(input ("b: "))
        print(cikarma(a,b))
    elif islem_adi == "carpma":
        a = int(input ("a: "))
        b = int(input ("b: "))
        print(carpma(a,b))
    elif islem_adi == "bolme":
        a = int(input ("a: "))
        b = int(input ("b: "))
        print(bolme(a,b))
    else:
        print("Hatalı islem adı girdiniz")

islem(toplama, cikarma, carpma, bolme, islem_adi)