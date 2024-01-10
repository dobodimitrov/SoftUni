count_of_nums = int(input())

for i in range(count_of_nums):
    current_num = int(input())
    if current_num % 2 == 0:
        continue
    else:
        print(f"{current_num} is odd!")
        break
else:
    print(f"All numbers are even.")