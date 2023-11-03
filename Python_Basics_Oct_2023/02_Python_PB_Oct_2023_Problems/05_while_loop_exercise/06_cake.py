cake_length = int(input())
cake_width = int(input())
cake_area = cake_length * cake_width
pieces_total = 0
is_enough = False

while pieces_total <= cake_area:
    command = input()
    if command == "STOP":
        is_enough = True
        break
    pieces_total += int(command)

if not is_enough:
    print(f"No more cake left! You need {pieces_total - cake_area} pieces more.")
else:
    print(f"{cake_area - pieces_total} pieces are left.")
