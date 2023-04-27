import json

#dict
person = {"name":"Ali","languages":["python","C#"]}

result =person["name"]
print(result)
result =person["languages"]
result = person["languages"][0]
print(result)


#json
person_string = '{"name":"Ali","languages":["python","C#"]}'
#JSON string to Dict
result = json.loads(person_string)
result =result['name']
print(type(result))

with open("person.json") as f:
    data = json.load(f)
    print(data)
