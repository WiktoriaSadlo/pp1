def f(n):
    x = int(input("Enter a number: "))
    for y in n:
        if y==x:
            return True
    return False

arr = [15,38,7,23,14]

print(f(arr))