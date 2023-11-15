def f(n):
    x=[]
    i=0
    while len(x)<n:
        if i==2 or i==3 or i==5 or i==7:
            x.append(i)
        elif i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i>2:
            x.append(i)
        i+=1
    return x[n-1]

print(f(1))
print(f(5))
print(f(9))