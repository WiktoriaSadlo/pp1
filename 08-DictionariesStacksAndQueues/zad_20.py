import json

file = open('euro.json','r')
content = json.loads(file.read())
file.close()

print("Date        Buying Rate     Selling Rate")
print("========================================")


for line in content["rates"]:
    x = line["ask"]
    x = str(x)
    if len(x) <=5:
        x += "0"
    print(line["effectiveDate"], "  ",x ,  "       ", line["bid"])