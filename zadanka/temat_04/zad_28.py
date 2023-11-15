def f(num):
    for x in range(len(num)):
        if num[x]!='0' and num[x]!='1':
            return False
    return True

print(f("101101")) #returns True
print(f("1311a10100")) #returns False
