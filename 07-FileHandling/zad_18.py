file1 = open('lorem_ipsum.txt','r')
file2 = open('zad_18.txt','w')

for line in file1:
    file2.write(line)

file1.close()
file2.close()