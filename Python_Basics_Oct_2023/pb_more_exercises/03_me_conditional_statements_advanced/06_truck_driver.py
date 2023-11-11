season = input()
total_km = float(input())
lv_per_km = 0

if season == "Spring" or season == "Autumn":
    if total_km <= 5000:
        lv_per_km = 0.75
    elif 5000 < total_km <= 10000:
        lv_per_km = 0.95
    if 10000 < total_km <= 20000:      # no matter the season
        lv_per_km = 1.45
elif season == "Summer":
    if total_km <= 5000:
        lv_per_km = 0.90
    elif 5000 < total_km <= 10000:
        lv_per_km = 1.10
    if 10000 < total_km <= 20000:  # no matter the season
        lv_per_km = 1.45
elif season == "Winter":
    if total_km <= 5000:
        lv_per_km = 1.05
    elif 5000 < total_km <= 10000:
        lv_per_km = 1.25
    if 10000 < total_km <= 20000:  # no matter the season
        lv_per_km = 1.45
# if 10000 < total_km <= 20000:      # no matter the season
#     lv_per_km = 1.45

salary_after_tax = 4 * (lv_per_km * total_km) * 0.9      # working 4 months and then 10% tax
print(f"{salary_after_tax:.2f}")
