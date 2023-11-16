pairs = int(input())
max_diff = 0
previous_sum = 0

for number_of_pairs in range(0, pairs):
    first_num = int(input())
    second_num = int(input())
    current_sum = first_num + second_num

    if current_sum == previous_sum or previous_sum == 0:
        previous_sum = current_sum
    else:
        diff = abs(previous_sum - current_sum)
        previous_sum = current_sum
        if diff > max_diff:
            max_diff = diff

if max_diff != 0:
    print(f"No, maxdiff={max_diff}")
else:
    print(f"Yes, value={previous_sum}")
