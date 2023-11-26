file1 = open('MeatAndFish.txt','r')
file2 = open('GrainsAndBread.txt','r')
file3 = open('shopping.txt','w')

for line in file1:
    file3.write(line)

for line in file2:
    file3.write(line)

file1.close()
file2.close()
file3.close()