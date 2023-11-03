def f(text):
    if len(text)==0:
        return ""
    for x in range(len(text)):
        if x==0:
            result=text[0]
        else:
            result+='-'
            result+=text[x]
    return result

print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))