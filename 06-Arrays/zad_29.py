def f(n1,n2):
    for x in n2:
        for y in range(len(n1)):
            if x==n1[y-1]:
                n1.pop(y-1)
    return n1

a1 = [4,36,12,28,9,44,5]
a2 = [5,1,36]

print(f(a1,a2))
