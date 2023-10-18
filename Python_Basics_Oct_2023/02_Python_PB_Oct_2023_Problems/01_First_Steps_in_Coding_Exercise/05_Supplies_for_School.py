PENS = 5.80
MARKERS = 7.20
DETERGENT = 1.20

pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input()) / 100

total_price = pens * PENS + markers * MARKERS + detergent * DETERGENT
price_after_discount = total_price - (total_price * discount)

print(price_after_discount)

