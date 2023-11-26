def f(arr):
    n=int(input('Enter a number: '))
    result=[]
    for x in arr:
        if x>n:
            result.append(x)
    return result

z = [7,3,8,5,2]
print(f(z))