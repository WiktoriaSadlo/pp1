sum = 0
i=0
x=int(input('Enter a number: '))

while x!=0:
    sum+=x
    x=int(input('Enter a number: '))
    i+=1

print(sum)
print(sum/i)
print(i)