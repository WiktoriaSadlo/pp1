def numbers (n):
    string = ""
    for x in range (1, n+1):
        string += str(x)
        string +=" "
    return string
    
print(numbers(12))