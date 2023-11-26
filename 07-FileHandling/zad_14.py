file = open('shopping_list.txt','a')
x = input('Enter a product: ')
while x!='':
    file.write("\n"+x)
    x = input('Enter a product: ')

file.close()