season = input()
gender = input()
student_count = int(input())
nights_count = int(input())
sport = ""
price_per_night = 0
discount = 1

if season == "Winter":
    if gender == "boys":
        sport = "Judo"
        price_per_night = 9.60
    elif gender == "girls":
        sport = "Gymnastics"
        price_per_night = 9.60
    elif gender == "mixed":
        sport = "Ski"
        price_per_night = 10.00
elif season == "Spring":
    if gender == "boys":
        sport = "Tennis"
        price_per_night = 7.20
    elif gender == "girls":
        sport = "Athletics"
        price_per_night = 7.20
    elif gender == "mixed":
        sport = "Cycling"
        price_per_night = 9.50
elif season == "Summer":
    if gender == "boys":
        sport = "Football"
        price_per_night = 15
    elif gender == "girls":
        sport = "Volleyball"
        price_per_night = 15
    elif gender == "mixed":
        sport = "Swimming"
        price_per_night = 20

if student_count >= 50:
    discount = 0.5
elif 20 <= student_count < 50:
    discount = 0.85
elif 10 <= student_count < 20:
    discount = 0.95

total_price = (price_per_night * student_count * nights_count) * discount
print(f"{sport} {total_price:.2f} lv.")
