vacation_price = float(input())
puzzle_quantity = int(input())
talking_doll_quantity = int(input())
teddy_bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

profit = puzzle_quantity * 2.60 \
        + talking_doll_quantity * 3.00 \
        + teddy_bear_quantity * 4.10 \
        + minion_quantity * 8.20 \
        + truck_quantity * 2.00

total_quantity = puzzle_quantity + talking_doll_quantity + teddy_bear_quantity + minion_quantity + truck_quantity

if total_quantity >= 50:
    profit *= 0.75

profit *= 0.9   # rent == 10% profit

if profit >= vacation_price:
    print(f'Yes! {profit - vacation_price:.2f} lv left.')
else:
    print(f'Not enough money! {vacation_price - profit:.2f} lv needed.')
