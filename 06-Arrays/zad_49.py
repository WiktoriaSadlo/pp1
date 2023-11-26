x = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for y in range (len(x)):
    for m in range(len(x[y])):
        x[y][m]=(y+1)*(m+1)

print(x)