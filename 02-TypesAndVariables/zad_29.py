import random
sum = 0

for y in range(3):
    x = int(random.randint(1,6))
    sum = sum + x
    print(x)

print(sum)