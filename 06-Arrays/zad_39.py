def f(arr):
    even = []
    odd = []
    for x in arr:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even + odd

z = [7,3,8,5,2]
print(f(z))