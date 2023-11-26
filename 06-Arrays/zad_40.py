import random

def f():
    result = ''
    for x in range(41):
        result+='-'
    result+='\n'
    for x in range(8):
        result+='|'
        a = random.randint(1,999)
        if a<10:
            result+='   '
        elif a<100:
            result+='  '
        else:
            result+=' '
        result+=str(a)
    result+='|'
    result+='\n'
    for x in range(41):
        result+='-'
    return result

print(f())
