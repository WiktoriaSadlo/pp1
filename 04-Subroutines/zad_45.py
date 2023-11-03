def f(expression):
    for x in range(len(expression)):
        if x==0:
            output = int(expression[x])
        elif x%2!=0 and expression[x]=='+':
            output+=int(expression[x+1])
        elif x%2!=0 and expression[x]=='-':
            output-=int(expression[x+1])
    return output

print(f('2+3'))
print(f('3+8+1'))
print(f('2+3-4+5-0'))
