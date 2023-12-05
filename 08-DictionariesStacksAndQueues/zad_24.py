def binary(number):
    stack = ''
    while number != 0:
        stack+=str(number%2)
        number//=2
    return stack[-1::-1]

print(binary(18))
print(binary(35))