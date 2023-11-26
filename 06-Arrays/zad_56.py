def f(n):
    result =[]
    for x in n:
        for y in x:
            result.append(y)
    return result


arr1 = [[2,3],[1,5]]
arr2 = [[5,0,3,7,5],[9,0,9,1,2]]
arr3 = [[2,1],[3,5],[7,4],[2,6]]
print(f(arr1))
print(f(arr2))
print(f(arr3))