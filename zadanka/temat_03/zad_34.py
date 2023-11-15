def f(coins):
    if coins//5>0:
        five = coins//5
        coins -= five*5
    if coins//2>0:
        two = coins//2
        coins -= two*2
    if coins == 1:
        one = 1
    return (f'5 zł - {five} \n2 zł - {two} \n1 zł - {one}')

print(f(18))