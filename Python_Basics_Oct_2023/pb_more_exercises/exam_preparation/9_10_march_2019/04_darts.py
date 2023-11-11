player = input()
command = input()
start_points = 301
total_points = 0
successful_shots = 0
unsuccessful_shots = 0
has_won = False

while command != "Retire":
    if total_points == start_points:
        has_won = True
        break

    current_points = int(input())

    if command == "Single":
        total_points += current_points
        if total_points > start_points:
            unsuccessful_shots += 1
            total_points -= current_points
            command = input()
            continue
        successful_shots += 1
    elif command == "Double":
        total_points += 2 * current_points
        if total_points > start_points:
            unsuccessful_shots += 1
            total_points -= 2 * current_points
            command = input()
            continue
        successful_shots += 1
    elif command == "Triple":
        total_points += 3 * current_points
        if total_points > start_points:
            unsuccessful_shots += 1
            total_points -= 3 * current_points
            command = input()
            continue
        successful_shots += 1
    if total_points == start_points:
        has_won = True
        break

    command = input()


if has_won:
    print(f"{player} won the leg with {successful_shots} shots.")
else:
    print(f"{player} retired after {unsuccessful_shots} unsuccessful shots.")
