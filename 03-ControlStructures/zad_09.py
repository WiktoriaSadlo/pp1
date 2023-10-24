test_tasks = 6
test_result = float(input('Enter your test result:'))

if test_result/test_tasks >= 0.5:
    print('Test passed')
else:
    print('Test faild')