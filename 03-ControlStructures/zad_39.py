a = int(input('Enter a lenght of the side of the rectangle:'))
b = int(input('Enter a lenght of the side of the rectangle:'))

for x in range (1,a+1):
    for y in range(1,b+1):
        if x == 1 or x==a:
            print('*', end=' ')
        elif y == 1 or y ==b:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
        
    