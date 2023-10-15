weight = int(input('Enter your weight in kg:'))
height = int(input('Enter your height in cm:'))
bmi = weight/(height/100)**2

if bmi<16:
    print('Wygłodzenie') 
elif bmi<17:
    print('Wychudzenie')
elif bmi<18.5:
    print('Niedowaga')
elif bmi<25:
    print('Prawidłowa masa ciała')
elif bmi<30:
    print('Nadwaga')
elif bmi<35:
    print('Otylość I stopnia')
elif bmi<40:
    print('Otyłość II stopnia')
else:
    print('Otyłość III stopnia')