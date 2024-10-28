import json

person_string = '{"name": "Ali", "languages":["Python", "C#"]}'

#Json to dictionary
result = json.loads(person_string)
print(type(result))
print(result)

# result = person["languages"][1]
# print(result)
# print(person.get("name"))