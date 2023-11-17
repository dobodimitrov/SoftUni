first_num_upper_lim = int(input())
second_num_upper_lim = int(input())
third_num_upper_lim = int(input())
is_prime = True

for first_num in range(1, first_num_upper_lim + 1):
    if first_num % 2 == 0:
        for second_num in range(1, second_num_upper_lim + 1):
            is_prime = True
            for i in range(2, int(second_num ** 0.5) + 1):
                    if second_num % i == 0:
                        is_prime = False
                        break
            if second_num >= 2:
                if is_prime:
                    for third_num in range(1, third_num_upper_lim + 1):
                        if third_num % 2 == 0:
                            print(f"{first_num} {second_num} {third_num}")