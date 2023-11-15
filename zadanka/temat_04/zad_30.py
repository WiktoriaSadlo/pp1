def f(num,even):
    sum = 0
    num = str(num)
    for x in range(len(num)):
        if even == True:
            if int(num[x])%2==0:
                sum+=int(num[x])
        else:
            if int(num[x])%2!=0:
                sum+=int(num[x])
    return sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))