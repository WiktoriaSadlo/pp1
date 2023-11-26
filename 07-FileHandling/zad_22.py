import random
file = open('random.txt','w')

for x in range(50):
    file.write(str(random.randint(100,999))+'\n')

file.close()