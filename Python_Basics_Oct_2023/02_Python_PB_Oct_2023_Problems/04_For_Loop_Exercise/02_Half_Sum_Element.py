import sys

count_of_numbers = int(input())
max_number = -sys.maxsize
total_sum = 0

for numbers in range(count_of_numbers):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(total_sum - 2 * max_number)}")
