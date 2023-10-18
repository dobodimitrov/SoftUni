# hours = int(input())
# minutes = int(input())
# minutes += 15
# hours += minutes // 60
# minutes %= 60
# if hours > 23:
#     hours = 0
# print(f'{hours}:{minutes:02d}')

hours_start = int(input())
minutes_start = int(input())

if 60 <= minutes_start + 15 <= 69 and hours_start + 1 <= 23:
    print(f'{hours_start + 1}:0{(minutes_start + 15) - 60}')

if 60 <= minutes_start + 15 <= 69 and hours_start + 1 > 23:
    print(f'0:0{(minutes_start + 15) - 60}')

if 60 <= minutes_start + 15 >= 69 and hours_start + 1 <= 23:
    print(f'{hours_start + 1}:{(minutes_start + 15) - 60}')

if 60 <= minutes_start + 15 >= 69 and hours_start + 1 > 23:
    print(f'0:{(minutes_start + 15) - 60}')

if minutes_start + 15 < 60:
    print(f"{hours_start}:{minutes_start + 15}")
