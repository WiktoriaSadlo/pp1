def f(password):
    if len(password)>=6:
        for x in range(len(password)):
            if password.count(password[x])>1:
                return False
        return True
    return False

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))