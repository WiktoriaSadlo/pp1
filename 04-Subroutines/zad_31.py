def f(x,y):
    sum = 0
    for i in range(x,y+1):
        if i%2==0 and i<0 :
            sum+=1
    return sum

print(f(-7,8))
print(f(-1,11))