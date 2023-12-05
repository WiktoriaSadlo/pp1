import csv
import json

with open('products.csv','r') as file1:
    data=[]
    json_file = open('products.json','w')
    csv_file = csv.DictReader(file1)
    for row in csv_file:
        data.append(row)
    json_file.write(json.dumps(data,indent=2))
    