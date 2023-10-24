amount = int(input('Enter an amount of money:'))
five = 0
two = 0
one = 0

while amount>0:
    if amount//5 >0:
        five = amount//5
        amount -= five*5
        if amount//2 >0:
            two = amount//2
            amount -= two*2
            if amount//1 > 0:
                one = amount//1
                amount -= one*1
        elif amount//1 > 0:
            one = amount//1
            amount -= one*1
    elif amount//2 >0:
        two = amount//2
        amount -= two*2
        if amount//1 > 0:
            one = amount//1
            amount -= one*1
    elif amount//1 > 0:
        one = amount//1
        amount -= one*1

print(f'The amount of PLN {amount} in coins:')
print(f'5 zł - {five}')
print(f'2 zł - {two}')
print(f'1 zł - {one}')