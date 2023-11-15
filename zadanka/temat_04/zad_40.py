def f(n):
    sum = 0
    n = str(n)
    for x in range(10):
        if n.count(str(x))>1:
            sum+=n.count(str(x))*x
    return sum

print(f(1027))
print(f(230335))
print(f(513553007))
