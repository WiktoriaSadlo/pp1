file = open('zad_23.txt','w')

for x in range(1,11):
    file.write(f'{x},{x**2},{x**3} \n')

file.close()