washing_product = input('Enter a washing product:')
rinse = True
spin = True
time=0

if washing_product=='jacket':
    time+=40
elif washing_product=='underwear':
    time+=70
else:
    time+=20

if rinse == True:
        time+=15
if spin==True:
        time+=9

print(f'Total washing time: {time}')