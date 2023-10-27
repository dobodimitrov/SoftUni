type_of_fuel = input()
litres_inside = int(input())

if litres_inside >= 25:
    if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
        print(f"You have enough {type_of_fuel.lower()}.")
    else:
        print("Invalid fuel!")
elif litres_inside < 25:
    if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
        print(f"Fill your tank with {type_of_fuel.lower()}!")
    else:
        print("Invalid fuel!")
