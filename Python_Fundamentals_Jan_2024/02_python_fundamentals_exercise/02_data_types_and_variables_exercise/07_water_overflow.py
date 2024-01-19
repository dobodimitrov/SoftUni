capacity = 255
number_of_lines = int(input())
total_liters = 0
for pours in range(number_of_lines):
    liters = int(input())
    if capacity - liters < 0:
        print("Insufficient capacity!")

    else:
        capacity -= liters
        total_liters += liters

print(total_liters)