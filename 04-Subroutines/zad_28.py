def f(binary_number):
    binary_number = str(binary_number)
    for x in binary_number:
        if x=='0' or x=='1':
            pass
        else:
            return False
    return True

print(f("101101"))
print(f(1101001))
print(f("11a4401"))