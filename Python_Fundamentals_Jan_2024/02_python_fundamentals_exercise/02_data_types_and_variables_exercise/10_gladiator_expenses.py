fights_lost = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_count = 0
sword_count = 0
shield_count = 0
armor_count = 0

for fight in range(1, fights_lost+1):
    if fight % 2 == 0:
        helmet_count += 1
    if fight % 3 == 0:
        sword_count += 1
        if fight % 2 == 0:
            shield_count += 1
            if shield_count % 2 == 0:
                armor_count += 1


total_expense = (helmet_price * helmet_count) + (sword_price * sword_count) + (shield_price * shield_count) + (armor_price * armor_count)

print(f"Gladiator expenses: {total_expense:.2f} aureus")