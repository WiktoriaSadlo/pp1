def f(n):
    result = []
    for i, v in enumerate(arr):
        if v not in arr[:i] and v not in arr[i+1:]:
            result.append(v)
    return result

arr = [2,3,2,5,8,1,9,8]
print(f(arr))
