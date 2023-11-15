decNum = int(input('Enter a decimal number:'))
binNum = ""

while decNum>=1:
    binNum += str(decNum%2)
    decNum//=2

print(binNum[::-1])