def f(n):
    list_primary=[2,3,5,7]
    for x in range(n*20):
        if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x>1:
            list_primary.append(x)
    return list_primary[n-1]


print(f(1))
print(f(5))