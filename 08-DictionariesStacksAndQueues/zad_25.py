import operator

def RPN_calculator(expresion):
    stack = []
    allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow
    }
    for x in expresion:
        if x.isdigit()==True:
            stack.append(int(x))
        elif x.isdigit()==False and x!='=':
            i=stack[-2]
            j=stack[-1]
            result = allowed_operators[x](i,j)
            stack.pop(-1)
            stack.pop(-1)
            stack.append(result)
        else:
            return stack[0]
        
print(RPN_calculator('23+='))
print(RPN_calculator('241+*='))
print(RPN_calculator('23+45+*='))
print(RPN_calculator('831+/32-4+*='))