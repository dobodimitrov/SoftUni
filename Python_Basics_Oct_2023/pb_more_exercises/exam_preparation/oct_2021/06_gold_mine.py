number_of_locations = int(input())
total_gold_mined = 0

for gold_mines in range(number_of_locations):
    expected_avg_yield = float(input())
    days_mining = int(input())
    for mining in range(days_mining):
        gold_mined_today = float(input())    # in kg
        total_gold_mined += gold_mined_today
    avg_yield = total_gold_mined / days_mining
    if avg_yield >= expected_avg_yield:
        print(f"Good job! Average gold per day: {avg_yield:.2f}.")
    elif avg_yield < expected_avg_yield:
        print(f"You need {(expected_avg_yield - avg_yield):.2f} gold.")
    avg_yield = 0
    total_gold_mined = 0
    