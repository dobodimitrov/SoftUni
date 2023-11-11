country = input()
instrument = input()
difficulty_points = 0
performance_points = 0

if country == "Russia":
    if instrument == "ribbon":
        difficulty_points = 9.100
        performance_points = 9.400
    elif instrument == "hoop":
        difficulty_points = 9.300
        performance_points = 9.800
    elif instrument == "rope":
        difficulty_points = 9.600
        performance_points = 9.000
elif country == "Bulgaria":
    if instrument == "ribbon":
        difficulty_points = 9.600
        performance_points = 9.400
    elif instrument == "hoop":
        difficulty_points = 9.550
        performance_points = 9.750
    elif instrument == "rope":
        difficulty_points = 9.500
        performance_points = 9.400
elif country == "Italy":
    if instrument == "ribbon":
        difficulty_points = 9.200
        performance_points = 9.500
    elif instrument == "hoop":
        difficulty_points = 9.450
        performance_points = 9.350
    elif instrument == "rope":
        difficulty_points = 9.700
        performance_points = 9.150

total_points = difficulty_points + performance_points
points_needed_percentage = (20 - total_points) / 20 * 100

print(f"The team of {country} get {total_points:.3f} on {instrument}.")
print(f"{points_needed_percentage:.2f}%")
