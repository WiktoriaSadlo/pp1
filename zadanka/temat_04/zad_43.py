def f(n):
    result = n[0]
    for x in range(len(n)):
        if n[x]==' ':
            result+=n[x+1]
    return result

print(f("Internet of Things"))
print(f("For Your Information"))
