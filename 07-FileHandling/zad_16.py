file_name = input('Enter a file name: ')
file = open(f'{file_name}','r')
i=0
for line in file:
    i+=1

print(i)