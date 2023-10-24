actor_name = input()
points_given = float(input())
number_of_judges = int(input())
total_judge_points = 0
points_total = 0 + points_given + total_judge_points

for mamkamu in range(1, number_of_judges + 1):
    judge_name = input()
    judge_points = float(input())
    total_judge_points += judge_points
    points_total += (judge_points * len(judge_name)) / 2
    if points_total > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_total:.1f}!")
        break
if points_total <= 1250:
    print(f'Sorry, {actor_name} you need {(1250.5 - points_total):.1f} more!')

