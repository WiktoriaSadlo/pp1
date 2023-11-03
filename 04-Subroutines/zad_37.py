def f(n):
    list_fib = []
    a = 0
    b = 1
    list_fib.append(a)
    list_fib.append(b)
    for x in range(n):
        b += a
        a = b - a
        list_fib.append(a)
    return list_fib[n]

print(f(5))
print(f(9))
        