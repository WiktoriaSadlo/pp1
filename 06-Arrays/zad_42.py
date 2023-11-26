import random

def rand_elem(arr):
    result = ''
    for x in range(3):
        index = random.randint(0,len(arr)-1)
        result+=str(arr[index])
        result+=', '
    return result[:-2]

a = [10,24,9,21,15]
print(rand_elem(a))