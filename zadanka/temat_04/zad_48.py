def f(n):
    con = 0
    for x in range(len(n)-1):
        con+=int(n[x])
    if con%7 == int(n[-1]):
        return True
    return False

print(f("1082"))
print(f('2035'))
print(f('1114'))