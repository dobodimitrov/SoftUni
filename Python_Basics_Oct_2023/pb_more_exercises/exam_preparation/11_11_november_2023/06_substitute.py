K = int(input())
L = int(input())
M = int(input())
N = int(input())

change_count = 0

for first_digit in range(K, 9):
    for second_digit in range(9, L - 1, -1):
        for first_digit_second_num in range(M, 9):
            for second_digit_second_num in range(9, N - 1, -1):
                if first_digit % 2 == 0 and second_digit % 2 != 0 and first_digit_second_num % 2 == 0 and second_digit_second_num % 2 != 0:
                    if change_count < 6:
                        if (first_digit * 10 + second_digit) != (first_digit_second_num * 10 + second_digit_second_num):
                            print(f'{first_digit}{second_digit} - {first_digit_second_num}{second_digit_second_num}')
                            change_count += 1
                        else:
                            print("Cannot change the same player.")
                            change_count += 1
                            break
