a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**0.5
print('Triangle area:', area )
print('Triangle circumference:', p*2)