def f(x,y):
    z = int(input('Enter a number: '))
    if z>=min(x,y) and z<=max(x,y):
        return True
    else:
        return False
        