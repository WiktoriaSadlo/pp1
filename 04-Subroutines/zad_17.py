def f(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n3 != n1:
        return True
    else:
        return False

print(f(int(input('Enter a number')),int(input('Enter a number')),int(input('Enter a number'))))