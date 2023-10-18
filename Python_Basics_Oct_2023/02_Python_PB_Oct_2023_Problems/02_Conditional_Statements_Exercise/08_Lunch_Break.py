# 1. Име на сериал – текст
# 2. Продължителност на епизод – цяло число в диапазона [10… 90]
# 3. Продължителност на почивката – цяло число в диапазона [10… 120
import math
show_name = input()
episode_duration = int(input())   #48
rest_duration = int(input())    #60


lunch_duration = 1/8 * rest_duration   #7.5
leisure_duration = 1/4 * rest_duration    #15
free_time = rest_duration - (lunch_duration + leisure_duration)

if free_time >= episode_duration:
    print(f"You have enough time to watch {show_name} and left with "
          f"{int(math.ceil(free_time - episode_duration))} minutes free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need "
          f"{int(math.ceil(episode_duration - free_time))} more minutes.")
