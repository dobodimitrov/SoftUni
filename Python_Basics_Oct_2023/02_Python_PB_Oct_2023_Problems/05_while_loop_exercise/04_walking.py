total_steps = 0
is_reached = True

while total_steps < 10000:
    current_steps = input()
    if current_steps == "Going home":
        current_steps = int(input())
        total_steps += int(current_steps)
        if total_steps < 10000:
            is_reached = False
        break
    total_steps += int(current_steps)

steps_difference = abs(10000 - total_steps)
if is_reached:
    print(f"Goal reached! Good job!")
    print(f"{steps_difference} steps over the goal!")
else:
    print(f"{steps_difference} more steps to reach goal.")
