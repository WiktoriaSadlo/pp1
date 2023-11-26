def identity_matrix(n):
    matrix = []
    for y in range(n):
        row = []
        for x in range(n):
            if x==y:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

print(identity_matrix(8))
