arr = [12,6,4,9,10]

def f(n):
    result=""
    for x in arr:
        if x>=10:
            result+=str(x)
        else:
            result+=" "
            result+=str(x)
        result+=": "
        for y in range(x):
            result+="*"
        result+="\n"
    return result

print(f(arr))