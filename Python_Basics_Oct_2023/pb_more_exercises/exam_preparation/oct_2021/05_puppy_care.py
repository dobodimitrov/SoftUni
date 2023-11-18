dog_food = int(input())     # in kg
command = input()
dog_food_in_grams = dog_food * 1000     # convert kg to g

while command != "Adopted":
    food_today = int(command)
    dog_food_in_grams -= food_today
    command = input()

if dog_food_in_grams >= 0:
    print(f"Food is enough! Leftovers: {dog_food_in_grams} grams.")
else:
    print(f"Food is not enough. You need {abs(dog_food_in_grams)} grams more.")