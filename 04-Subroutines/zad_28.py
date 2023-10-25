def f(binary_number):
    y = str(binary_number)
    for x in range(len(y)):
        if y[x]!= '0' or y[x]!= '1':
            return False 
    return True

print(f(101101))
print(f("1311a10100"))