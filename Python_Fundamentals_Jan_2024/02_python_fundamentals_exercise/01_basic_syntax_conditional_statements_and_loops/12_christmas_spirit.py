quantity = int(input())
remaining_days = int(input())
total_cost = 0
total_spirit = 0
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for current_day in range(1, remaining_days + 1):
    if current_day % 2 == 0:
        total_cost += quantity * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity * (tree_garland_price + tree_skirt_price)
        total_spirit += 3 + 10
    if current_day % 5 == 0:
        total_cost += quantity * tree_lights_price
        total_spirit += 17
        if current_day % 3 == 0:


