basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

def person(a,b):
    person = {}
    for key,value in a.items():
        person.update({key:value})
    for key,value in b.items():
        person.update({key:value})
    return person

print(person(basic_data,advanced_data))

