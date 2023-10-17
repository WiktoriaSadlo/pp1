number = input('Enter credit card number:')
card_num = number[:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:]
print(card_num)