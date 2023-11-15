arr = [2,3,7,5,4]

#a
print(arr)

#b
print(len(arr))

#c
print(arr[0])

#d
print(arr[1])

#e
print(arr[-1])

#f
print(arr[len(arr)-1])

#g
print(arr[0]+arr[-1])

#h do naprawy!
index = len(arr)//2 if len(arr)%2==0 else (len(arr)-1)//2
print(arr[index])

#i
for i in arr:
    print(i, end=", ") if i!=arr[-1] else print(i,end="")