
record = float(input())
distance = float(input())
time_1_meter = float(input())

import math

time_lost = 12.5 * math.floor(distance / 15) #съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди
ivans_time = distance * time_1_meter + time_lost
time_needed = (ivans_time - record)

if ivans_time < record:
    print(f'Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_needed:.2f} seconds slower.')
