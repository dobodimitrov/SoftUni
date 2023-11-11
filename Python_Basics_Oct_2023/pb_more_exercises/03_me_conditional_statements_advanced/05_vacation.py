budget = float(input())
season = input()
accommodation = ""
price = 0
place = ""

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        place = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = 0.8 * budget
    elif season == "Winter":
        place = "Morocco"
        price = 0.6 * budget
elif budget > 3000:
    accommodation = "Hotel"
    price = 0.90 * budget
    if season == "Summer":
        place = "Alaska"
    else:
        place = "Morocco"

print(f"{place} - {accommodation} - {price:.2f}")
