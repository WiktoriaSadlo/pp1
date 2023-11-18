arr = ['Genowefa','Onfury','Celestyna','Alojzy','Pankracy']
x = arr[0]

for y in arr:
    if len(y)>len(x):
        x=y

print(x)