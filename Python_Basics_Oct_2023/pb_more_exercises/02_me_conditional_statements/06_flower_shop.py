import math
MAGNOLIA = 3.25
HYACINTH = 4.00
ROSE = 3.50
CACTUS = 8.00

magnolia_total = int(input()) * MAGNOLIA
hyacinth_total = int(input()) * HYACINTH
rose_total = int(input()) * ROSE
cactus_total = int(input()) * CACTUS
gift = float(input())

total_money_made = (magnolia_total + hyacinth_total + rose_total + cactus_total) * 0.95    # taxes
money_difference = abs(total_money_made - gift)
if total_money_made >= gift:
    print(f"She is left with {math.floor(money_difference)} leva.")
else:
    print(f"She will have to borrow {math.ceil(money_difference)} leva.")
