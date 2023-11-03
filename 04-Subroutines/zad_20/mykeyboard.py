def read_number():
    x = int(input('Enter a number: '))
    y = int(input('Enter a number: '))
    return (f'{x} + {y} = {x+y}')

if __name__=="__main__":
    print(read_number())