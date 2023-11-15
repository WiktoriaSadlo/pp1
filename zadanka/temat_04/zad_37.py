def f(n):
    a=0
    b=1
    for x in range(n-1):
        a=b-a
        b=a+b
        if x==n-2:
            return a
        
print(f(5))
print(f(9))