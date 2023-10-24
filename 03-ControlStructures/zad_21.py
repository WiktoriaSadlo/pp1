x = int(input('Enter a number:'))
y = int(input('Enter a number:'))

if x>y:
    print(f'Numbers in ascending order: {y} , {x}')
elif x == y :
    print(f'x = {x} is equal y = {y}')
else:
    print(f'Numbers in ascending order: {x} , {y}')