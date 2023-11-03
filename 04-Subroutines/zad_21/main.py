import mymath

x = mymath.generate_number()
y = int(input('Enter a number from 1 to 9: '))

if x==y:
    print('You won the game!!!')
else:
    print(f'Sorry you lost :( The number was {x}')