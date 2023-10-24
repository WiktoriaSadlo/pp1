time = input('Enter time (24-hour format):')

if len(time)==5:
    if int(time[:2])>12:
        print(f'Time in 12-hour format: {int(time[:2])-12}{time[2:]} pm')
    else: 
        print(f'Time in 12-hour format: {time} pm')
else:
    print(f'Time in 12-hour format: {time} am')