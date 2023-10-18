SQ_METER_PRICE = 7.61
discount = 0.82

sq_meter_total = int(input())

price_before_discount = sq_meter_total * SQ_METER_PRICE
price_after_discount = price_before_discount * discount
saved_money = price_before_discount - price_after_discount

print(f'The final price is {price_after_discount}.')
print(f'The discount is: {saved_money}')
