# json.py

import json

person = {
    "name": "Amr",
    "age": 20,
    "city": "Almaty"
}

json_string = json.dumps(person)

print(json_string)


data = json.loads(json_string)

print(data["name"])


with open("person.json", "w") as file:
    json.dump(person, file)


with open("person.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)
