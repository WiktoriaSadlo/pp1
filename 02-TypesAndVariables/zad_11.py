fathers_income = int(input('Enter father’s income: '))
mothers_income = int(input('Enter mother’s income: '))
number_of_people = int(input('Enter number of people in your family:'))
print('Total income: ', fathers_income + mothers_income)
print('Income per person: ', (fathers_income + mothers_income)/number_of_people)