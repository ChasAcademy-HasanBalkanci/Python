"""
try:
    file = open("newfile.txt", "r", encoding="utf-8")
except FileNotFoundError as ex:
    print(ex)
finally:
    print("File closed")
    file.close()

"""


"""
file =  open("newfile.txt", "r", encoding="utf-8")

for i in file:
    print(i, end="")

file.close()

"""

file =  open("newfile.txt", "r", encoding="utf-8")
content = file.read()

print(content)

file.close()