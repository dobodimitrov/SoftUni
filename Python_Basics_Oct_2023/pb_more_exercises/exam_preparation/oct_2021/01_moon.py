import math
average_speed = float(input())
fuel_per_100_km = float(input())

total_km = 384_400 * 2
total_time_travelling = math.ceil(total_km / average_speed) + 3      # spent 3 hours on the Moon
total_fuel = (fuel_per_100_km * total_km) / 100

print(total_time_travelling)
print(int(total_fuel))
