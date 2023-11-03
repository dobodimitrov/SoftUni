length = int(input())
width = int(input())
height = int(input())
volume = length * width * height
has_enough_space = False
total_boxes = 0

while volume > total_boxes:
    command = input()
    if command == "Done":
        has_enough_space = True
        break
    total_boxes += int(command)

space_left_or_needed = abs(volume - total_boxes)

if has_enough_space:
    print(f"{space_left_or_needed} Cubic meters left.")
if not has_enough_space:
    print(f"No more free space! You need {space_left_or_needed} Cubic meters more.")
