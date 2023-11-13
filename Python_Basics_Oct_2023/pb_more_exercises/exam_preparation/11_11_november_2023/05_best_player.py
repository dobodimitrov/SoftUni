command = input()
most_goals = 0
has_hattrick = False
best_player = ""

while command != "END":
    goals = int(input())
    player = command
    if goals > most_goals:
        most_goals = goals
        best_player = player
    if goals >= 3:
        has_hattrick = True
    if goals >= 10:
        break
    command = input()        # name of player

print(f"{best_player} is the best player!")
if has_hattrick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")