number_of_cats = int(input())
small_cats = 0
big_cats = 0
huge_cats = 0
total_food_weight = 0

for cats in range(number_of_cats):
    food_weight = float(input())      # per day
    total_food_weight += food_weight
    if 100 <= food_weight < 200:
        small_cats += 1
    elif 200 <= food_weight < 300:
        big_cats += 1
    elif 300 <= food_weight < 400:
        huge_cats += 1

total_food_weight_in_kg = total_food_weight / 1_000     # turn g into kg
total_price = total_food_weight_in_kg * 12.45

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")