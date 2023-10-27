rest_days = int(input())
work_days = 365 - rest_days    # year - rest days
norm_minutes_played = 30000

rest_days_minutes_played = rest_days * 127
work_days_minutes_played = work_days * 63
total_minutes_played = rest_days_minutes_played + work_days_minutes_played    # per year

remaining_minutes = abs(total_minutes_played - norm_minutes_played)
total_hours_played = remaining_minutes // 60
total_minutes_difference = remaining_minutes % 60

if total_minutes_played > norm_minutes_played:
    print(f"Tom will run away")
    print(f"{abs(total_hours_played)} hours and {abs(total_minutes_difference)} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{abs(total_hours_played)} hours and {abs(total_minutes_difference)} minutes less for play")
