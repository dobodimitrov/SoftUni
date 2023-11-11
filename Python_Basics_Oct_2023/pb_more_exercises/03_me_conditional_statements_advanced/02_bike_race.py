juniors = int(input())
seniors = int(input())
trace = input()
entrance_fee_juniors = 0
entrance_fee_seniors = 0

if trace == "trail":
    entrance_fee_juniors = 5.50
    entrance_fee_seniors = 7.00
elif trace == "cross-country":
    entrance_fee_juniors = 8.00
    entrance_fee_seniors = 9.50
    if juniors + seniors >= 50:
        entrance_fee_juniors *= 0.75
        entrance_fee_seniors *= 0.75
elif trace == "downhill":
    entrance_fee_juniors = 12.25
    entrance_fee_seniors = 13.75
elif trace == "road":
    entrance_fee_juniors = 20.00
    entrance_fee_seniors = 21.50

total_money_raised = (entrance_fee_juniors * juniors + entrance_fee_seniors * seniors) * 0.95     # expenses
print(f"{total_money_raised:.2f}")
