import random

x = int(input('Enter the number of rolled:'))

for y in range(x):
    z = random.randint(1,6)
    print(z)
    if z==1 or z==6:
        print('True')
        break
    elif y==(x-1):
        print('False')
    else:
        continue