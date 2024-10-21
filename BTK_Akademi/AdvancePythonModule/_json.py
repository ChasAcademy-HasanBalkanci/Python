from calendar import Day
import json
# person = '{"name": "Ali", "languages":["Python", "C++"]}' # JSON string.
# # JSON to DICt to use in Python
# result = json.loads(person) #************
# print(type(result))
# result = result["languages"][1]
# print(result)
# with open("person.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     print(data["languages"][1])
person_dict = {
    "name": "Ali", 
    "languages":["Python", "C++"],
    "city": "Istanbul"

}
person_str = json.dumps(person_dict)
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(result)
print(person_dict)
# result = json.dumps(person_dict)
# #print(type(result))
# with open("person.json", "w", encoding="utf-8") as file:
#     json.dump(person_dict, file)

