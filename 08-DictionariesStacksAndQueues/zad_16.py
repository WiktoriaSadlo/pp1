Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
Hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(a,b):
    result = ""
    for x in a:
        for key,value in x.items():
            if key == "name":
                result+=value
                result+=", "
    if b == "kraków":
        return(f'Hotels in Kraków: {result[:-2]}')
    else:
        return(f'Hotels in Sopot: {result[:-2]}')
    
def avg_price(a,b):
    sum=0
    for x in a:
        for key,value in x.items():
            if key == "price":
                sum += value
    if b == 'kraków':
        return (f'The average price in Kraków is {sum/len(a)}')
    else:
        return (f'The average price in Sopot is {sum/len(a)}')
    
def cheaper(a,b):
    krk_sum=0
    for x in a:
        for key,value in x.items():
            if key == "price":
                krk_sum += value
    krk_sum/=len(a)
    sop_sum=0
    for x in b:
        for key,value in x.items():
            if key == "price":
                sop_sum += value
    sop_sum/=len(b)
    if krk_sum>sop_sum:
        return ('Cheaper is Sopot')
    elif krk_sum<sop_sum:
        return ('Cheaper is Kraków')
    else:
        return('Sopot and Kraków is the same')

print(hotel_list(Hotels_in_Sopot,"sopot"))
print(avg_price(Hotels_in_Krakow,"krakó"))
print(cheaper(Hotels_in_Krakow,Hotels_in_Sopot))