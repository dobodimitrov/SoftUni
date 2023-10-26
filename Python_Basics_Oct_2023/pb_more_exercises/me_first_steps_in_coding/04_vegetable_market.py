vegetables_per_kilo_price = float(input())
fruit_per_kilo_price = float(input())
vegetables_quantity = int(input()) # in kg
fruit_quantity = int(input()) # in kg

fruit_total_price = fruit_per_kilo_price * fruit_quantity
vegetables_total_price = vegetables_per_kilo_price * vegetables_quantity
total_price_in_euro = (fruit_total_price + vegetables_total_price) / 1.94

print(f'{total_price_in_euro:.2f}')
