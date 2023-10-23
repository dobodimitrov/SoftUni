month = input()
total_nights_spent = int(input())
studio_a_night_price = 0
apartment_a_night_price = 0

if month == "May" or month == "October":
    studio_a_night_price = 50
    apartment_a_night_price = 65
    if 7 < total_nights_spent <= 14:
        studio_a_night_price *= 0.95
    if total_nights_spent > 14:
        studio_a_night_price *= 0.7
        apartment_a_night_price *= 0.9
elif month == "June" or month == "September":
    studio_a_night_price = 75.20
    apartment_a_night_price = 68.70
    if total_nights_spent > 14:
        studio_a_night_price *= 0.8
        apartment_a_night_price *= 0.9
elif month == "July" or month == "August":
    apartment_a_night_price = 77.00
    studio_a_night_price = 76.00
    if total_nights_spent > 14:
        apartment_a_night_price *= 0.9

total_apartment_price = apartment_a_night_price * total_nights_spent
total_studio_price = studio_a_night_price * total_nights_spent

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
