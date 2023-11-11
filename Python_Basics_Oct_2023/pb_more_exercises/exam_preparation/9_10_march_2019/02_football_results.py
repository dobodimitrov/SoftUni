wins = 0
draws = 0
losses = 0
first_digit = 0
second_digit = 0
for games in range(1, 3+1):
    game_result = input()
    for index, digit in enumerate(game_result):
        if index == 0:
            first_digit = int(digit)
        if index == 2:
            second_digit = int(digit)
            if first_digit > second_digit:
                wins += 1
                break
            elif first_digit < second_digit:
                losses += 1
                break
            elif first_digit == second_digit:
                draws += 1
                break

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")
