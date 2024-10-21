# import re
# text = "ABC 123s XYZ 456 @&% 300 0 a17 xx278909988 A12"
# #pattern = r"\d\d\d"
# pattern = r"^A*"

# #match = re.search(pattern, text)
# #match = re.findall(pattern, text)
# matches = re.finditer(pattern, text)
# for i in matches:
#     print(i.group())
# import re
# text = "BTK Akademi ile Python kurs tarihleri 15-May-2025 15/May/2025 15.05.2025. Telefon numaralarimiz +90-530-999-9999 +90 530 999 9999. Mail adreslerimiz abc@gmail.com abc@gmail.co.tr"
# text_1 = "Ali ata bak\nAli naber\nAli bana bak"
# # pattern = r"\d{2}-[a-zA-Z]{3}-\d{4}"
# # pattern = r"\d{2}[-./][a-zA-Z0-9]{2,3}[-./]\d{4}"
# #pattern = r"\d{2}[-./]([a-zA-Z]{3}|\d{2})[-./]\d{4}"
# # pattern = r"[\w]+@[\w]+\.[\w]+( |[\w]+\.[\w]+)"
# pattern = r"^Ali"
# matches = re.finditer(pattern, text_1)
# for i in matches:
#     print(i.group())

import re

pattern = "^hello+"
string = "helloworld \nhello again"

for i in re.finditer(pattern, string, re.MULTILINE):
    print(i.group())