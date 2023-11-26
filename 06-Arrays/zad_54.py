import numpy as np

def transpose_matrix1(n):
    # 1 sposób
    x = np.array(n)
    return x.transpose()

def transpose_matrix2(n):
    # 2 sposób
    x=[]
    for m in range (len(n[0])):
        row = []
        for j in range (len(n)):
            row.append(0)
        x.append(row)
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j]=n[j][i]
    return x

arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[12,7],[4,5],[3,8]]
arr3 = [[1,2,3,4,5],[6,7,8,9,0]]
arr4 = [[5,6,7,8]]
print(transpose_matrix2(arr1))
print(transpose_matrix2(arr3))
print(transpose_matrix2(arr4))

