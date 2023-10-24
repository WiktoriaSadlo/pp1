correct_PIN = 2334

for x in range(3):
    pin = int(input('Enter a PIN:'))
    if pin == correct_PIN:
        print('Correct PIN!')
        break
    elif x == 2 and pin != correct_PIN:
        print('Incorrect.')
        print('Sorry, your payment card has been blocked')
    else:
        print('Incorrect...')
