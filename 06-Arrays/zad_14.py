arr = [[2,5,4],[9,0,3]]

#a
print(arr)

#b
print(f'Rows:{len(arr)}')
print(f'Columns:{len(arr[0])}')

#c
for x in arr:
    if x==5:print(x)

#d
for x in arr:
    if x==3:print(x)

#e
for x in arr[1]:
    print(x, end=" ")