def f(arr,n):
    num = 0
    for x in arr:
        if x==n:
            num+=1
    return num

tup = (50,20,40,50,30,50)
print(f(tup,50))