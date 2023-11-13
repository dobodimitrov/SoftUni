cargo_count = int(input())
bus = 0
truck = 0
train = 0
total_weight = 0
total_price = 0

for cargo in range(0, cargo_count):
    current_weight = int(input())    # in tons
    total_weight += current_weight
    if current_weight <= 3:
        bus += current_weight
        total_price += 200 * current_weight
    elif 4 <= current_weight <= 11:
        truck += current_weight
        total_price += 175 * current_weight
    else:
        train += current_weight
        total_price += 120 * current_weight

avg_price = total_price / total_weight      # avg price per ton
bus_percentage = (bus / total_weight) * 100
truck_percentage = (truck / total_weight) * 100
train_percentage = (train / total_weight) * 100

print(f"{avg_price:.2f}")
print(f"{bus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
