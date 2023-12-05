import json

file = open('data_19.json','r')
file1= json.load(file)
file.close()
file2 = open('limited.json','w')

for line in file1:
    del line['gender']
    del line['age']
    del line['year_of_study']
    del line['email']

json.dump(file1,file2,indent=2)
