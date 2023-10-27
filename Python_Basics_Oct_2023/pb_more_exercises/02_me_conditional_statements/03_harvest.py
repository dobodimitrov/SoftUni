import math

area = int(input())
grapes_per_sq_meter = float(input())    # in kg
needed_litres = int(input())
number_of_workers = int(input())

grapes_total = area * grapes_per_sq_meter
grapes_for_wine = (0.4 * grapes_total) / 2.5

more_needed_or_left = abs(needed_litres - grapes_for_wine)
liters_per_worker = more_needed_or_left / number_of_workers
if grapes_for_wine < needed_litres:
    print(f"It will be a tough winter! More {math.floor(more_needed_or_left)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(grapes_for_wine)} liters.")
    print(f"{math.ceil(more_needed_or_left)} liters left -> {math.ceil(liters_per_worker)} liters per person.")
