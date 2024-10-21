# import datetime
# result = dir(datetime.datetime)
# print(result)
from datetime import datetime
simdi = datetime.now()
result = datetime.now().today()
result = datetime.ctime(simdi)
result = datetime.strftime(simdi, "%Y.%B.%d %X %H:%M:%S")
print(result)