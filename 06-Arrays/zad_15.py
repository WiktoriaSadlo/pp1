arr = [[1,3,5],[8,7,2]]

#a
print(arr[0][0]+arr[-1][-1])

#b
index = len(arr)//2 if len(arr)%2==0 else (len(arr)-1)//2
print(arr[0][index]+arr[1][index])

#c
sum = 0
for x in arr[-1]:
    sum+=x
print(sum)