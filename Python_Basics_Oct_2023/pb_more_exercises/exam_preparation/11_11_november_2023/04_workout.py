import math
days_training = int(input())
first_day_distance = float(input())      # in km
total_distance = 0 + first_day_distance
goal_distance = 1_000

for training in range(1, days_training + 1):
    percentage_increase = int(input())
    increase = percentage_increase / 100
    total_distance += first_day_distance + first_day_distance * increase
    first_day_distance = first_day_distance + first_day_distance * increase

if total_distance >= goal_distance:
    print(f"You've done a great job running {math.ceil(total_distance - goal_distance)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(goal_distance - total_distance)} more kilometers")
