#do naprawy

def f(number,even):
    sum = 0
    if even == True:
        for x in range(len(str(number))):
            if number[x]%2==0:
                sum+=x
    elif even == False:
        for x in range(len(str(number))):
            if  number[x]%2!=0:
                sum+=x
    else:
        return "Idiot"
    return sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))