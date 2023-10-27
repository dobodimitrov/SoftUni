import math

days = int(input())
food_given = int(input())        # in kg
dog_food_per_day = float(input())    # in kg
cat_food_per_day = float(input())          # in kg
turtle_food_per_day = float(input()) / 1000       # in g; convert to kg by dividing by 1000

food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_per_day) * days
food_difference = abs(food_needed - food_given)
if food_needed <= food_given:
    print(f"{math.floor(food_difference)} kilos of food left.")
else:
    print(f"{math.ceil(food_difference)} more kilos of food are needed.")
