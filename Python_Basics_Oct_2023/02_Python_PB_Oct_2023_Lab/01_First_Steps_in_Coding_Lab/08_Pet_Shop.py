DOG_FOOD_PRICE = 2.50
CAT_FOOD_PRICE = 4

dog_food_quantity = int(input())
cat_food_quantity = int(input())

total_price = dog_food_quantity * DOG_FOOD_PRICE + cat_food_quantity * CAT_FOOD_PRICE

print(f'{total_price} lv.')