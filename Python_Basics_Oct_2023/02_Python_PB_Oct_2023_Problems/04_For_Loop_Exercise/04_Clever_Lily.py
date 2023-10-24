age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money_saved = 0
count_of_toys = 0
total_money = 0
brother_money = 0

for years in range(1, age + 1):
    if years % 2 == 0:
        money_saved += 10
        total_money += money_saved
        brother_money += 1
    elif years % 2 == 1:
        count_of_toys += 1
total_money += count_of_toys * toy_price - brother_money
if total_money >= washing_machine_price:
    print(f"Yes! {(total_money - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - total_money):.2f}")

