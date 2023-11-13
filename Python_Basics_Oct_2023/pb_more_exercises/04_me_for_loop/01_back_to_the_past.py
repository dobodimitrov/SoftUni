# inherited_money = float(input())
# year_needed = int(input())
# money_spent = 0
#
# for money_spent_even in range(1800, year_needed + 1, 2):
#     money_spent += 12000
#
# for aging in range(19, 18 + year_needed - 1800, 2):
#     money_spent += 12000 + 50 * aging
#
# money_left_or_needed = abs(inherited_money - money_spent)
#
# if inherited_money >= money_spent:
#     print(f"Yes! He will live a carefree life and will have {money_left_or_needed:.2f} dollars left.")
# else:
#     print(f"He will need {money_left_or_needed:.2f} dollars to survive.")

inherited_money = float(input())
year_needed = int(input())
money_spent = 0
age = 19
for years in range(1_800, year_needed + 1):
    if years % 2 == 0:
        money_spent += 12_000
    else:
        for aging in range(19, 18 + year_needed - 1800, 2):
            money_spent += 12_000 + 50 * age
            age += 2
            break

money_left_or_needed = abs(inherited_money - money_spent)

if inherited_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have {money_left_or_needed:.2f} dollars left.")
else:
    print(f"He will need {money_left_or_needed:.2f} dollars to survive.")

