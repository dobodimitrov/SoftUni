budget = float(input())
flour_per_kg_price = float(input())
pack_of_eggs_price = 0.75 * flour_per_kg_price
liter_of_milk_price = 1.25 * flour_per_kg_price
colored_eggs = 0
loafs_count = 0
total_cost = 0
price_per_loaf = flour_per_kg_price + pack_of_eggs_price + liter_of_milk_price

while total_cost <= budget:
    if total_cost + price_per_loaf >= budget:
        break
    else:
        total_cost += price_per_loaf
    colored_eggs += 3
    loafs_count += 1
    if loafs_count % 3 == 0:
        colored_eggs -= (loafs_count - 2)
    for next_three_loafs in range(1, 3+1):
        if total_cost + (liter_of_milk_price + pack_of_eggs_price) >= budget:
            break
        else:
            total_cost += (liter_of_milk_price + pack_of_eggs_price)
        colored_eggs += 3
        loafs_count += 1

        if loafs_count % 3 == 0:
            colored_eggs -= (loafs_count - 2)



print(f"You made {loafs_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget - total_cost:.2f}BGN left.")
