def f(n):
    y=0
    for x in range(1,7):
        if n.count(str(x))>=y:
            y=n.count(str(x))
            z=x
    return z

print(f("5233165554211"))
print(f('2133'))