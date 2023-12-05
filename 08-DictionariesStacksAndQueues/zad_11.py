import json

movie = {
    "title" : "Harry Potter",
    "year" : "2001",
    "actor" : ["Daniel Radcliffe","Emma Woston","Rupert Grint"],
    "oscar" : False,
    "type" : "fantasy"
}

with open("favourite.json", 'w') as file:
    json.dump(movie,file,indent = 4)

file.close()