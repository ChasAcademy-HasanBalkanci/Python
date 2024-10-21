# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content2 = file.write("deneme\ndeneme2\n")
#     print(content2)


# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nEmel Turan")
#     file.write("\nTuket Turan")

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = content + "Son Satir\n" # write at the end of the file
#     content = "Ilk Satir\n" + content # write at the end of the file
#     file.seek(0)
#     file.write(content)


with open("newfile.txt", "r+", encoding="utf-8") as file:
    list_text = file.readlines()
    list_text.(4, "4\n")
    file.seek(0)
    file.writelines(list_text)
 

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())



# with open("newfile.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

