# To open file open() is used.
# the method of opening file is "r" for read mode and "w" for write mode and 
# "a" for append mode and "r+" for read and write mode open("filename", "mode")
# mode:
# r - read mode. if the file does not exist, the operation will fail.
# w - write mode. The current data in the file will be deleted. If there is a no file with that name, it will be created.

""" 
file = open("newfile.txt", "w")
file.close()

"""
"""
file = open("C:\\Users\\swhas\\Desktop\\newfile.txt", "w")
print(file)

"""

"""
file = open("newfile.txt", "w", encoding="utf-8")
#file.write("Hakan Balkanci ")
file.write("Python")
file.close()
"""

# a - append mode. The data will be appended to the end of the file. If the file does not exist, it will be created.

"""
file = open("newfile.txt", "a", encoding="utf-8")
#file.write(" Python")
file.write(" hasan")
file.close()

"""


# r+ - read and write mode

# x - exclusive creation. If the file already exists, the operation will fail.

file = open("newfile.txt", "x", encoding="utf-8")
file.write("x mode\n")
file.close()
# The "with" statement is used to open a file and automatically close it when the block is exited.

