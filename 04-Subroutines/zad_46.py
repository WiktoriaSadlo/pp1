def f(x,y):
    sum = 0 
    for z in range(x,y+1):
        if z%2==0 and z%3==0 and z%4!=0:
            sum+=z
    return sum

print(f(1,20))
print(f(10,30))