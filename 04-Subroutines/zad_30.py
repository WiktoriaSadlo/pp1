def f(number,even):
    sum = 0
    number=str(number)
    if even == True:
        for x in range(len(number)):
            if int(number[x])%2==0:
                sum+=int(number[x])
    elif even == False:
        for x in range(len(number)):
            if  int(number[x])%2!=0:
                sum+=int(number[x])
    else:
        return "Idiot"
    return sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))