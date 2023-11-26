def f(x,y):
    m = []
    n = []

    for i in range(y):
        n.append(0)
    for j in range(x):
        m.append(n)

    return m

print(f(3,5))