ROSE = 5.00
DAHLIA = 3.80
TULIP = 2.80
NARCISSUS = 3.00
GLADIOLA = 2.50

flower_type = input()
flower_number = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    if flower_number > 80:
        price = 0.9 * ROSE
    else:
        price = ROSE
elif flower_type == "Dahlias":
    if flower_number > 90:
        price = 0.85 * DAHLIA
    else:
        price = DAHLIA
elif flower_type == "Tulips":
    if flower_number > 80:
        price = 0.85 * TULIP
    else:
        price = TULIP
elif flower_type == "Narcissus":
    if flower_number < 120:
        price = 1.15 * NARCISSUS
    else:
        price = NARCISSUS
elif flower_type == "Gladiolus":
    if flower_number < 80:
        price = 1.2 * GLADIOLA
    else:
        price = GLADIOLA

total_price = flower_number * price
money_left_or_needed = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and {money_left_or_needed:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left_or_needed:.2f} leva more.")
