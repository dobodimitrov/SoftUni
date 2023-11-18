import math
width = float(input())
length = float(input())
height = float(input())
average_astronaut_height = float(input())

rocket_capacity = width * length * height     # in m**3   (cubic meters)
room_capacity = (average_astronaut_height + 0.40) * 2 * 2    # in m**3   (cubic meters)

number_of_people = math.floor(rocket_capacity / room_capacity)

if 3 <= number_of_people <= 10:
    print(f"The spacecraft holds {number_of_people} astronauts.")
elif number_of_people < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
