count_of_numbers = int(input())
group_1 = 0 # 200 > number
group_2 = 0 # 200 <= number <= 399
group_3 = 0 # 400 <= number <= 599
group_4 = 0 # 600 <= number <= 799
group_5 = 0 # 800 <= number

for numbers in range(count_of_numbers):
    number = int(input())
    if number < 200:
        group_1 += 1
    elif 200 <= number < 400:
        group_2 += 1
    elif 400 <= number < 600:
        group_3 += 1
    elif 600 <= number < 800:
        group_4 += 1
    elif number >= 800:
        group_5 += 1
print(f"{(group_1 / count_of_numbers * 100):.2f}%")
print(f"{(group_2 / count_of_numbers * 100):.2f}%")
print(f"{(group_3 / count_of_numbers * 100):.2f}%")
print(f"{(group_4 / count_of_numbers * 100):.2f}%")
print(f"{(group_5 / count_of_numbers * 100):.2f}%")
