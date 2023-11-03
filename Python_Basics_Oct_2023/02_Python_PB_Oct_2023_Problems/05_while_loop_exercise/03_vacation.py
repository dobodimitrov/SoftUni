vacation_money_needed = int(input())
available_money = int(input())
consecutive_days_spending = 0
current_money = 0
days_total = 0
has_enough = True
action = ""

while vacation_money_needed > available_money:
    action = input()
    current_money = int(input())
    days_total += 1
    if action == "spend":
        available_money -= current_money
        consecutive_days_spending += 1
        if available_money < 0:
            available_money = 0
        if consecutive_days_spending == 5:
            has_enough = False
            break
    if action == "save":
        available_money += current_money
        consecutive_days_spending = 0

if not has_enough:
    print("You can't save the money.")
    print(f"{days_total}")
if has_enough:
    print(f"You saved the money for {days_total} days.")
