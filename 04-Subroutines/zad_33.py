def f(n):
    string = ''
    if n>0:
        string += '*'
        if n>1:
            for x in range(1,n):
                string+='/*'
    return string

print(f(4))
print(f(1))