x = [[-38, 19], [5,40],[-7,11],[29,16]]

def smallest(n):
    row = 0
    column = 0
    min = n[0][0]
    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j]<=min:
                row = i
                column = j
                min = n[i][j]
    return f'Smallest value: {min}, row: {row}, column: {column}'

def largest(n):
    row = 0
    column = 0
    max = n[0][0]
    for i in range(len(n)):
        for j in range(len(n[i])):
            if n[i][j]>=max:
                row = i
                column = j
                max = n[i][j]
    return f'Largest value: {max}, row: {row}, column: {column}'
    
print(smallest(x))
print(largest(x))