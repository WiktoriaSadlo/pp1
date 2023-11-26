x = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]]

first = []
for y in x:
    first.append(y[0])

last = []
for y in x:
    last.append(y[len(y)-1])

for i in range(len(x)):
    x[i][0]=last[i]

for j in range(len(x)):
    x[j][-1]=first[j]

print(x)
print(last)
print(first)