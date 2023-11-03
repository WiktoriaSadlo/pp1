for x in range (1,8):
    for y in range (7):
        if x+7*y<10:
            print(' ',end='')
        print(x+7*y, end=' ')
    print()