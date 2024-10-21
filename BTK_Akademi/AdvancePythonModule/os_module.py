import os
# result = dir(os)
# result = os.name
# result = os.getcwd()
# os.chdir('..')
# os.mkdir("deneme")
# print(result)
# os.makedirs("deneme/newdirectory", exist_ok=True)
'''
result =  os.listdir("D:\\GitHubChassAcadmey/Python/BTK_Akademi/AdvancePythonModule")
filter_file = (file for file in result if file.endswith(".py"))
while True:
    try:
        print(next(filter_file))
    except StopIteration:
        break
'''
#import datetime
#result = os.stat("D:\\GitHubChassAcadmey/Python/BTK_Akademi/AdvancePythonModule/os_module.py")
#result = result.st_size/1024
#result = datetime.datetime.fromtimestamp(result.st_ctime).strftime("%Y-%m-%d %H:%M:%S") #result.st_ctime
#result = datetime.datetime.fromtimestamp(result.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
#os.system("notepad.exe")
#os.rename("deneme/newdirectory", "deneme/newdirectory2")
#os.rmdir("deneme/newdirectory2")
#os.removedirs("deneme/newdirectory2")
#result = os.path.dirname(os.path.abspath("datatyperna.py"))
#result = os.path.exists("os_module.py")
#result = os.path.isdir("D:\\GitHubChassAcadmey/Python/BTK_Akademi/AdvancePythonModule")

print(result)
