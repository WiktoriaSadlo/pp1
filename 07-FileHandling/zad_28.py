import re

file = open('lorem_ipsum.txt','r')
y=re.findall("[A-Za-z]{6}[A-Za-z]*",file.read())
print(y)
