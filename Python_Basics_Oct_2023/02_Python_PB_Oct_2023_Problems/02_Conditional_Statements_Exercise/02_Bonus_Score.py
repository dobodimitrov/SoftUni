# · Ако числото е до 100 включително, бонус точките са 5;
# · Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# · Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
# · Допълнителни бонус точки (начисляват се отделно от предходните)
#
# o За четно число à + 1 т.
# o За число, което завършва на 5 à + 2 т.

number = int(input())
bonus_points = 0

if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = 0.2 * number
elif number > 1000:
    bonus_points = 0.1 * number

extra_bonus_points = 0


if number % 2 == 0:
    extra_bonus_points = 1

if number % 10 == 5:
    extra_bonus_points = 2

bonus_points = bonus_points + extra_bonus_points

print(bonus_points)
print(bonus_points + number)
