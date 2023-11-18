arr = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i==j: arr[i][j]=1

for x in arr:
    print(x)