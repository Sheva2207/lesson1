def get_discount(one, two, delimiter = '&') :
    new_string = str(f'{one}{delimiter}{two}')
    return new_string
a = get_discount(1, 'Pyton')
print(a.upper())

