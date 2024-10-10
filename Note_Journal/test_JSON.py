
import json
from random import randint
from datetime import datetime
str_json = """{

"response" : {
    "count":456457,
    "item":[
        {
        "first_name":"Елезавета",
        "id":346474754,
        "last_name":"Сопова",
        "can_accens_closed": true
        },
        {
        "first_name":"Роман",
        "id":346463,
        "last_name":"Синев",
        "can_accens_closed": true
        }
        ]
    }
}"""
print(type(str_json))
data = json.loads(str_json)
print(type(data))

print(type(data["response"]["item"]))

for item in (data["response"]["item"]):
    print(item)
    print(type(item))
    print(item['first_name'], item["last_name"])
    del item["id"]
    item["lackeds"] = randint(100,9999)
    item['a'] = None
    item['now'] = datetime.now().strftime("%d.%m.%y")
print((data["response"]["item"]))
new_json = json.dumps(data, indent= 2)
#with open("my_gson","a") as file:
#    json.dump(data, file, indent=3)

#print(new_json)

#print(json.loads(new_json))

with open("my_gson","r") as file:
    data = json.load(file)
print(data)