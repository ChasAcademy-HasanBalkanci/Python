import re
from unittest import result
#result = dir

# '''
# Here are some of the most important and useful re methods in Python:

# re.search(): Searches for the first occurrence of the pattern in the string.
# Example: re.search("hello", "hello world")

# re.match(): Searches for the pattern at the beginning of the string.
# Example: re.match("hello", "hello world")

# re.findall(): Finds all occurrences of the pattern in the string and returns them as a list.
# Example: re.findall("hello", "hello world hello")

# re.sub(): Replaces occurrences of the pattern in the string with a replacement string.
# Example: re.sub("hello", "hi", "hello world")

# re.split(): Splits the string into substrings based on the pattern.
# Example: re.split("hello", "hello world hello")

# re.compile(): Compiles a regular expression pattern into a regular expression object, which can be used for matching using its match(), search(), and findall() methods.
# Example: re.compile("hello").search("hello world")

# re.escape(): Escapes special characters in a string so that it can be used as a regular expression pattern.
# Example: re.escape("hello world")

# re.findall() with groups: Finds all occurrences of the pattern in the string and returns them as a list of tuples, where each tuple contains the groups of the match.
# Example: re.findall(r\"(\w+) (\w+)\", "hello world hello")
# '''
text = "Python Kursun : Pyxxon Programlama Rehberiniz | 40 saat \nPyt9hon st saaaaaat123 satttt sat aasat Hasan"
#result = re.findall("Python", str)
#result = re.split(":", text)
#result = re.sub(r"123", "Python", text)
#result = re.search("Python", text)
#result = result.span()
#result = result.group()
#result = re.findall("[abc]", text)
#result = re.findall(r"[^a-z\s0-9]", text) # = re.findall("[A-Z]", text)
#result = re.findall(r"Py..on", text)
#result = re.findall(r"^Python", text)
#result_compile = re.findall(r"[^Python]", text, re.MULTILINE)
#result = re.findall(r"saat$", text)
#result = re.findall(r"hone$", text)
#result = re.findall(r"sa?t?", text)
result = re.findall(r"\B[0-9]", text)
result_1 = re.findall(r"\b[0-9]", text)
print(result)
print(result_1)
#print(result_compile)