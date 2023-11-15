arr = [1,2,3,4,5]

#a
arr[0]=arr[0]-1

#b
arr[-1]=arr[-1]+4

#c
index = len(arr)//2 if len(arr)%2==0 else (len(arr)-1)//2
arr[index]=arr[index]*2

print(arr)