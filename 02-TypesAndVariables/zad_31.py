import random

x = random.randint(1,6)
y = int(input('Enter the number between 1 and 6:'))

if x==y:
    print(True, x)
else:
    print(False, x)