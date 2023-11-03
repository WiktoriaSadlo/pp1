n = int(input('Podaj liczbę:'))

for x in range(n+1):
    if x>2 and x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
        print(x, end=' ')
    elif x==2 or x==3 or x==5 or x==7:
        print(x, end=' ')
