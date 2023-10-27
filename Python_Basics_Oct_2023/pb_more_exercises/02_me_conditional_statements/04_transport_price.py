km = int(input())
time_of_day = input()
taxi_total_price = 0 + 0.70
bus_total_price = 0
train_total_price = 0
cheapest = ""

if km < 20:
    if time_of_day == "day":
        taxi_total_price += km * 0.79
        print(f"{taxi_total_price:.2f}")
    elif time_of_day == "night":
        taxi_total_price += km * 0.90
        print(f"{taxi_total_price:.2f}")
elif 20 <= km < 100:
    bus_total_price += km * 0.09
    print(f"{bus_total_price:.2f}")
elif km >= 100:
    train_total_price += km * 0.06
    print(f"{train_total_price:.2f}")

