floors = int(input())
rooms = int(input())    # per floor
floor_letter = " "

for current_floor in range(floors, 1 - 1, -1):
    if current_floor == floors:
        floor_letter = "L"
    elif current_floor % 2 == 0:
        floor_letter = "O"
    else:
        floor_letter = "A"
    for current_room in range(rooms):
        print(f"{floor_letter}{current_floor}{current_room}", end = " ")
    print()