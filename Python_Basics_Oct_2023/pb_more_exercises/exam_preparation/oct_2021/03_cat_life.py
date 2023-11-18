import math
breed = input()
sex = input()
life_expectancy = 0
is_invalid = False

if sex == "m":
    if breed == "British Shorthair":
        life_expectancy = (13 * 12) / 6
    elif breed == "Siamese":
        life_expectancy = (15 * 12) / 6
    elif breed == "Persian":
        life_expectancy = (14 * 12) / 6
    elif breed == "Ragdoll":
        life_expectancy = (16 * 12) / 6
    elif breed == "American Shorthair":
        life_expectancy = (12 * 12) / 6
    elif breed == "Siberian":
        life_expectancy = (11 * 12) / 6
    else:
        is_invalid = True

elif sex == "f":
    if breed == "British Shorthair":
        life_expectancy = (14 * 12) / 6
    elif breed == "Siamese":
        life_expectancy = (16 * 12) / 6
    elif breed == "Persian":
        life_expectancy = (15 * 12) / 6
    elif breed == "Ragdoll":
        life_expectancy = (17 * 12) / 6
    elif breed == "American Shorthair":
        life_expectancy = (13 * 12) / 6
    elif breed == "Siberian":
        life_expectancy = (12 * 12) / 6
    else:
        is_invalid = True

if is_invalid:
    print(f"{breed} is invalid cat!")
else:
    print(f"{math.floor(life_expectancy)} cat months")
