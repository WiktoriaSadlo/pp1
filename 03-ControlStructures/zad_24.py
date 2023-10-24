before_price = int(input('Enter a price before sale:'))
after_price = int(input('Enter a price after sale:'))
discount = (before_price - after_price)/before_price*100

if discount>= 10:
    print(f'Buy the product!! Product price reduced by {discount}% ')
else:
    print(f"Don't buy it. Product price reduced by only {discount}%")