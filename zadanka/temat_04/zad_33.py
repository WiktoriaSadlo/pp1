def f(n):
    string=''
    for x in range(n):
        if x == 0:
            string+='*'
        else:
            string+='/*'
    return string

print(f(8))
print(f(1))