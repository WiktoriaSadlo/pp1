file = open('student.txt','w')
x=input('Enter a text: ')
while x!='':
    file.write(x+'\n')
    x=input('Enter a text: ')

file.close()