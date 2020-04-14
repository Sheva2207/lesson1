def get_discount(one, two, delimiter = '&') :
    new_string = str(f'{one}{delimiter}{two}')
    return new_string
a = get_discount(1, 'Pyton')
print(a.upper())

def format_price(price):
    price = int(price)
    price_see = f'Price: {price} rub.'
    return price_see
b = format_price(56.24)
print(b)