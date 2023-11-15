def f(signs):
    people = 0
    for x in range(len(signs)):
        if signs[x]=='+':
            people+=1
        else:
            people-=1
        if people>=3:
            return True
    return False

print(f("+-+++-+---")) #returns True
print(f("+-+-+-+-")) #returns False
print(f("+-++-+--")) #returns False
print(f("+-++-++-+---")) #returns True
