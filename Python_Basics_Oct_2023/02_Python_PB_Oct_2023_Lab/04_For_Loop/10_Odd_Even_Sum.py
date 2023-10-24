count_of_numbers = int(input())
even_sum = 0
odd_sum = 0

for numbers in range(count_of_numbers):
    current_number = int(input())
    if numbers % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")