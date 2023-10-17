pi = 3.14
obwod = int(input('Wprowadź obwód:'))
promien = obwod/(2*pi)
srednica = pi*promien**2
if srednica>=50:
    print('Drzewo może być ścięte')
else:
    print('Drzewo nie może być ścięte')