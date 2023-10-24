number_decimal = int(input('Enter a number:'))
remainder = ''

while number_decimal >= 1:
    remainder += str(number_decimal%2)
    number_decimal//=2

print(remainder[::-1])