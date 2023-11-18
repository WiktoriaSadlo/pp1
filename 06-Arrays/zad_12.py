def f(arr):
    even=0
    for x in arr:
        if x%2==0: even+=1 
    return even

print(f([34,7,19,4,21,8]))