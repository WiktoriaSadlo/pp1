x = (10,20,30,40,50)
z = list(x)
for y in range(len(x)):
    z[len(x)-1-y]=x[y]
z=tuple(z)
print(z)