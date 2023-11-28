import re

file = open('grades.txt','r')
reader = file.read()

grades = re.findall('\d.{2}',reader)
sum=0
for i in grades:
    sum+=float(i)

print(sum/len(grades))
