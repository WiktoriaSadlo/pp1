def calculate_for():
    for x in range(1,11):
        print(f'1/{x} = {1/x}')

def calculate_while():
    i=1
    while i<=10:
        print(f'1/{i} = {1/i}')
        i+=1
    
calculate_for()
calculate_while()
