def f(n):
    people = 0
    for x in range(len(n)):
        if n[x]=='+':
            people += 1
            if people>=3:
                return True
        else:
            people -= 1
    return False

    
    
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))