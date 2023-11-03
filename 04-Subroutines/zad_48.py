def f(product_code):
    sum=0
    for x in range(0,len(product_code)-1):
        sum+=int(product_code[x])
    if int(product_code[-1])==sum%7:
        return True
    return False

print(f('1082'))
print(f('2035'))
print(f('1114'))
print(f('7071'))