q_1 = input('Are you interested in computer science? (Y/N): ')
q_2 = input('Do you like playing computer games? (Y/N): ')
q_3 = input('Do you have an Instagram account? (Y/N): ')

if q_1 == 'Y':
    print('Interested in computer science: Yes')
elif q_1 == 'N':
    print('Interested in computer science: No')
else:
    print('Error')

if q_2 == 'Y':
    print('Playing computer games: Yes')
elif q_2 == 'N':
    print('Playing computer games: No')
else:
    print('Error')

if q_3 == 'Y':
    print('Has an Instagram account: Yes')
elif q_3 == 'N':
    print('Has an Instagram account: No')
else:
    print('Error')