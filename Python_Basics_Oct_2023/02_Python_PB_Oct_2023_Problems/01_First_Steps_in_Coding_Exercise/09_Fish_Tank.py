length = int(input())
width = int(input())
height = int(input())
percentage_occupied_space = float(input()) / 100

capacity = length * width * height
litres = capacity * 0.001
litres_needed = litres * (1 - percentage_occupied_space)

print(litres_needed)