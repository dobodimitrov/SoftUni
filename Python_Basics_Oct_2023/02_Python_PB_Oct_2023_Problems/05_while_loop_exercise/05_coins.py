target_money = float(input())
target_money_pennies = target_money * 100
coins_count = 0

while target_money_pennies > 0:
    if target_money_pennies >= 200:
        target_money_pennies -= 200
        coins_count += 1
    elif target_money_pennies >= 100:
        target_money_pennies -= 100
        coins_count += 1
    elif target_money_pennies >= 50:
        target_money_pennies -= 50
        coins_count += 1
    elif target_money_pennies >= 20:
        target_money_pennies -= 20
        coins_count += 1
    elif target_money_pennies >= 10:
        target_money_pennies -= 10
        coins_count += 1
    elif target_money_pennies >= 5:
        target_money_pennies -= 5
        coins_count += 1
    elif target_money_pennies >= 2:
        target_money_pennies -= 2
        coins_count += 1
    elif target_money_pennies >= 1:
        target_money_pennies -= 1
        coins_count += 1

print(coins_count)
