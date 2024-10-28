import os
import datetime
import re

# # Get the current working directory
# current_dir = os.getcwd()
# print("Current working directory:", current_dir)

# # Specify the directory path
# new_dir = './Python/lesson/Exercises'

# # Check if the directory exists
# if os.path.exists(new_dir):
#     # Change the working directory
#     os.chdir(new_dir)
#     print("Changed working directory to:", new_dir)
# else:
#     print("Directory does not exist:", new_dir)

# # Get the new working directory
# new_dir = os.getcwd()
# #os.mkdir("new_dir")
# #os.rmdir("new_dir")
# print("New working directory:", new_dir)

# result = os.listdir('../..')
# result = os.stat("D:\\GitHubChassAcadmey/Python/BTK_Akademi/AdvancePythonModule/os_module.py")
# #result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_atime).strftime("%Y-%m-%d %H:%M:%S")
# os.listdir
# #os.rename("deneme/newdirectory", "hi/newdirectory2")
# print(result)
# os.chdir("./Python/lesson/Exercises")
# current_dir = os.getcwd()

# if "new_dir" in os.listdir():
#     os.rmdir("new_dir")
# os.mkdir("new_dir")
# os.removedirs("new_dir")
# result = os.listdir()
# print(current_dir)
# print(result)
#os.chdir("./Python/lesson/Exercises")
print(os.getcwd())
print(os.listdir())
#result = os.path.abspath("main.py")
#result = os.path.dirname(os.path.abspath("class_demo.py"))
#result = os.path.dirname("D:\\GitHubChassAcadmey\\Python\\lesson\\Exercises\\class_demo.py")
result = os.path.exists("class_demo.py")
result = os.path.isfile("D:\\GitHubChassAcadmey\\Python\\lesson\\Exercises")
print(result)
