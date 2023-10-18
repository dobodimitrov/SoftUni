# · Декорът за филма е на стойност 10% от бюджета.
# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

budget = float(input())
actor_count = int(input())
clothing_price = float(input())

decor_price = 0.1 * budget
clothing_discount = 0.1 * clothing_price

if actor_count > 150:
    clothing_price = clothing_price - clothing_discount

money_left_or_needed = abs(budget - (clothing_price * actor_count + decor_price))

if decor_price + clothing_price * actor_count > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_left_or_needed:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left_or_needed:.2f} leva left.")

# · Ако парите за декора и дрехите са повече от бюджета:
# o "Not enough money!"
# o "Wingard needs {парите недостигащи за филма} leva more."
# · Ако парите за декора и дрехите са по малко или равни на бюджета:
# o "Action!"
# o "Wingard starts filming with {останалите пари} leva left."
