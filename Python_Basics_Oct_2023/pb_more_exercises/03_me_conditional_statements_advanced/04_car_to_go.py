budget = float(input())
season = input()
class_type = ""
car_type = ""
car_price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.35 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.65 * budget
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.45 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.80 * budget
elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    car_price = 0.90 * budget

print(class_type)
print(f"{car_type} - {car_price:.2f}")
