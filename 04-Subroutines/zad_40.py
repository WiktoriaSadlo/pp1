def f(number):
    z=0
    str_num = str(number)
    for x in range(10):
        if str_num.count(str(x))>1:
            z+=str_num.count(str(x))*x
    return z
        
print(f(1027))
print(f(230335))
print(f(513553007))
