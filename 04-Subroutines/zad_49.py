def f(dice):
    z = 0
    for x in range(10):
        y = dice.count(str(x))
        if y>z:
            z=y
            x_odp = x
    return x_odp

print(f("5233165554211"))
print(f("2133"))