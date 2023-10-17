description = 'Mr. John May, born on 1998-02-16'
name = description[4:8]
surname = description[9:12]
initial = description[4] + description[9]
born = description[-10:]
print(name)
print(surname)
print(initial)
print(born)