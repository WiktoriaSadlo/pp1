def f(coins):
    if coins//5>0:
        five = coins//5
        coins -= five*5
    if coins//2>0:
        two = coins//2
        coins -= two*2
    if coins == 1:
        one = 1
    return five + two + one

print(f(23))
print(f(8))