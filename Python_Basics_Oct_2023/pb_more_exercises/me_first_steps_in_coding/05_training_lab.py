import sys
length = float(input()) * 100
width = float(input()) * 100

path = 100    # width
desks_per_row = (width - path) // 70
rows = length // 120
number_of_seats = rows * desks_per_row - 3    # 1 for the door; 2 for the cathedra

print(int(number_of_seats))
