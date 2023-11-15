a = 0
b = 1

for x in range(20):
    print(a, end=' ')
    a = b - a
    b = a + b