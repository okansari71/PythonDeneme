import json

person_string ='{"name":"Ali","languages":["python","C#"]}'

# JSON string to Dict
# result = json.loads(person_string)
# print(type)
# result =result["name"]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

# print(result)

person_dict = {
    "name":"Ali",
    "languages":["Python","C#"]
}

# #Dict to JSON string
# result = json.dumps(person_dict)

# print(type(result))

# with open("person.json","w") as f:
#     json.dump(person_dict, f)
