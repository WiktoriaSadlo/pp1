# p1
"""
def f1(amount_to_pay):
    if amount_to_pay>=5:
        five = amount_to_pay//5
        amount_to_pay-=five*5
    if amount_to_pay>=2:
        two = amount_to_pay//2
        amount_to_pay-=two*2
    if amount_to_pay==1:
        one = 1
    return five + two + one
"""
#print(f1(23))

#p2
""""
def f2(n1,n2,n3):
    if n1!=n2 and n2!=n3 and n3!=n1:
        return True
    else:
        return False

print(f2(4,8,5))
print(f2(2,9,2))
"""
#p3

def f(name):
    result=name[0]
    for x in range(len(name)):
        if name[x]==' ':
            result+=name[x+1]
    return result

#print(f3('Internet of Things'))
#print(f3('For Your Information'))
#print(f3('Python'))
