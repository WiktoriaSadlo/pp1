#a
def SeconLargest(arr):
    a = arr.index(max(arr))
    b = list(arr)
    b[a]=0
    return max(b)

#b
def differnce(arr):
    a = max(arr)
    b = min(arr)
    return a-b

#c
def mediana(arr):
    a=list(arr)
    a.sort()
    if len(a)%2==0:
        sum = a[(len(a)-1)//2]+arr[len(a)//2]
        return sum/2
    else:
        return a[len(a)//2]

#d
def maxAndMin(arr):
    result = []
    result.append(min(arr))
    result.append(max(arr))
    return result

#e
def stringResult(arr):
    result=''
    for x in arr:
        result+=str(x)
        result+='-'
    return result[:-1]

z = (7,3,8,5,2)
print(SeconLargest(z))
print(differnce(z))
print(mediana(z))
print(maxAndMin(z))
print(stringResult(z))