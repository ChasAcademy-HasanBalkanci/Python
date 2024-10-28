import re

# result = dir(re)
# print(result)
str = "Python Kursun : Pyxxon Programlama Rehberiniz | 40 saat ssgggggt \nPyt9hon sat st saaaaaat123 satttt sat aasat Hasan"
# result = re.findall("Python", str)
#result = re.split(" ", str)

#result =  re.sub(r"\s", "-", str)
#result = re.search("Python", str)
# = result.start()
#result = result.end()
#result = result.group()
#result = result.string()
result = re.findall(r"^\w", str)



print(result)