from datetime import datetime
import re
result = datetime.now()
result_1 = datetime.today()
result_2 = datetime.ctime(result)
print(result.year)
print(result_1.year)
print(result_2)
