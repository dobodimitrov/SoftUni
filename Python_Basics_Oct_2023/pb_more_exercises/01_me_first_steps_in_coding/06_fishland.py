mackerel_price = float(input())     #skumriq
sprat_price = float(input())    #caca
bonito_quantity = float(input())    # in kg    #palamud
saffron_quantity = float(input())    # in kg    #safrid
mussels_quantity = float(input())    # in kg    #midi

bonito_price = 1.6 * mackerel_price
saffron_price = 1.8 * sprat_price
MUSSELS_PRICE = 7.50

total_price = bonito_quantity * bonito_price + saffron_price * saffron_quantity + MUSSELS_PRICE * mussels_quantity

print(f'{total_price:.2f}')
