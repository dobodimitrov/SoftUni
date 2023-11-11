budget = float(input())
category = input()
people = int(input())

transport_money = 0
VIP = 499.99
NORMAL = 249.99

if 1 <= people < 5:
    transport_money = 0.75 * budget
elif 5 <= people < 10:
    transport_money = 0.6 * budget
elif 10 <= people < 25:
    transport_money = 0.5 * budget
elif 25 <= people < 50:
    transport_money = 0.4 * budget
elif people >= 50:
    transport_money = 0.25 * budget

money_left = budget - transport_money
money_vip = abs(money_left - people * VIP)
money_normal = abs(money_left - people * NORMAL)

if category == "VIP":
    if money_left >= people * VIP:
        print(f"Yes! You have {money_vip:.2f} leva left.")
    else:
        print(f"Not enough money! You need {money_vip:.2f} leva.")
elif category == "Normal":
    if money_left >= people * NORMAL:
        print(f"Yes! You have {money_normal:.2f} leva left.")
    else:
        print(f"Not enough money! You need {money_normal:.2f} leva.")
