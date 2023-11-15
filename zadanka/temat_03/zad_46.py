for x in range(0,7):
    for y in range(1,50,7):
        if (x+y)<10:
            print(f' {x+y}',end=' ')
        else:
            print(x+y, end=' ')
    print()