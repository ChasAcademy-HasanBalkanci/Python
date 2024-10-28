import json
import os

person_string = '{"name": "Ali", "languages":["Python", "C#"]}'

#Json to dictionary
# result = json.loads(person_string)
# print(type(result))
# os.getcwd()
# os.chdir("D:\\GitHubChassAcadmey\\Python\\lesson\\Exercises")
#with open("person.json", "r") as file:
#    person = json.load(file)
#    print(person)

# result = person["languages"][1]
# print(result)

# result = person["languages"][1]
# print(result)
# print(person.get("name"))

person_dict = {
    "name": "Ali",
    "languages": ["Python", "C++"],
    "city": "Istanbul"
}

# result = json.dumps(person_dict)
# print(type(result))
# print(result)

os.chdir("D:\\GitHubChassAcadmey\\Python\\lesson\\Exercises")
# with open("person.json", "w", encoding="utf-8") as file:
#     json.dump(person_dict, file, indent=4)
#     print(f"Saved!")

# with open("person.json", "r", encoding="utf-8") as file:
#     person = json.load(file)
#     print(person)

person_dict_1 = json.loads(person_string)
result = json.dumps(person_dict_1, indent=4, sort_keys=True)
print(person_dict_1, "\n", result)
