def f(amount_to_pay):

    five = 0
    if amount_to_pay//5!=0:
        five = amount_to_pay//5
        amount_to_pay-=5*five

    two = 0
    if amount_to_pay//2!=0:
        two = amount_to_pay//2
        amount_to_pay-=2*two

    one = 0
    if amount_to_pay//1!=0:
        one = amount_to_pay//1
        amount_to_pay-=1*one

    return five + two + one  

print(f(23))
print(f(8))
print(f(2))