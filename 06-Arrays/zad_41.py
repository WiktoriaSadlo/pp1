def f(arr1,arr2):
    for x in arr2:
        if arr1.count(x)==0:
            return False
    return True

a1 = [16,3,7,12,9]
a2 = [16,3,9]

print(f(a1,a2))