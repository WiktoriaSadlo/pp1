pin = 1357

for x in range (3):
    entPin = int(input('Enter a PIN:'))
    if entPin == pin:
        print('Correct PIN')
        break
    elif x!=2:
        print('Incorrect, try again.')
    else:
        print('Incorrect. Sorry, your payment card has7777 been blocked.')