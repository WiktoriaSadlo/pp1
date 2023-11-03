def f(n1,n2,operator):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '%':
        return n1 % n2
    elif operator == '**':
        return n1 ** n2
    
print(f(2,3, "+")) #returns 5
print(f(2,3, "%")) #returns 2
print(f(2,3, "**")) #returns 8
print(f(2,3, "*")) #returns 6
print(f(2,3, "-")) #returns -1
