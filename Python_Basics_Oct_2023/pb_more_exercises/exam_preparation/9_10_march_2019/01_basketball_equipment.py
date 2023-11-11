import math
tennis_racket_price = float(input())
tennis_racket_counter = int(input())
sneakers_counter = int(input())
sneakers_price = 1/6 * tennis_racket_price
other_equipment_price = 0.2 * (sneakers_price * sneakers_counter + tennis_racket_counter * tennis_racket_price)

rackets_total = tennis_racket_price * tennis_racket_counter
sneakers_total = sneakers_counter * sneakers_price
price_total = rackets_total + sneakers_total + other_equipment_price

djokovic_pays = 1/8 * price_total
sponsors_pay = 7/8 * price_total

print(f"Price to be paid by Djokovic {math.floor(djokovic_pays)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_pay)}")
