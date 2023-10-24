num_of_products = int(input('Enter a number of products:'))
price = float(input('Enter a price of product:'))
to_pay = 0

for x in range(1,num_of_products+1):
    if x>2:
        to_pay += price*0.75
    else:
        to_pay += price

print(f'Amount to pay:{to_pay}')