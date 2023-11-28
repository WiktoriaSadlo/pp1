import csv

with open('zad_24.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if int(row['age'])<=30:
            print(row['first_name'],end=' ')
            print(row['last_name'],end=' ')
            print(row['email'])