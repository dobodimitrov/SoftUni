destination = input()
minimal_budget = float(input())
saved_money = 0

while destination != "End":
    current_money = float(input())
    saved_money += current_money
    if saved_money >= minimal_budget:
        print(f"Going to {destination}!")
        saved_money = 0
        destination = input()
        if destination != "End":
            minimal_budget = float(input())

