def f(name):
    acronym = name[0]
    for x in range(len(name)):
        if name[x]==' ':
            acronym+=name[x+1]
    return acronym

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))