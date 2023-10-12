x = int(input('Enter a number:'))
y = int(input('Enter a second number:'))

z = x
x = y
y = z

print('Value of x:', y)
print('Value of y:', x)
print('Value of x after swapping:', x)
print('Value of y after swapping:', y)