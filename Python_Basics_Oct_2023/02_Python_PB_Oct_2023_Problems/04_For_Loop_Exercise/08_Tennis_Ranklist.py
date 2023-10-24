count_of_tournaments = int(input())
start_points = int(input())
total_points = 0
games_won = 0

for tournaments in range(1, count_of_tournaments + 1):
    stage_reached = input()
    if stage_reached == "W":
        total_points += 2000
        games_won += 1
    elif stage_reached == "F":
        total_points += 1200
    elif stage_reached == "SF":
        total_points += 720

final_points = total_points + start_points
average_points = total_points / count_of_tournaments
win_rate = (games_won / count_of_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {int(average_points)}")
print(f"{win_rate:.2f}%")
