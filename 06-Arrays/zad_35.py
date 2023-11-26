x = ("Seven",[10,20,30],(5,15,25))

def f(n,n1):
    n = list(n)
    for y in n:
        if type(y)==list:
            for i in y:
                if i==n1:
                    return i
        elif type(y)==tuple:
            y=list(y)
            for i in y:
                if i==n1:
                    return i
        else:
            if y==n1:
                return y
            
print(f(x,"Seven"))
print(f(x,30))