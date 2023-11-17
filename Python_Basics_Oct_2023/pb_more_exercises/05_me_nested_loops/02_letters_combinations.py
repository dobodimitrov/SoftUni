# start_letter = input()
# end_letter = input()
# excluded_letter = input()
#
# combinations = []
#
# start_ord = ord(start_letter)
# end_ord = ord(end_letter)
#
# for i in range(start_ord, end_ord + 1):
#     for j in range(start_ord, end_ord + 1):
#         for k in range(start_ord, end_ord + 1):
#             combination_str = ''.join(map(chr, [i, j, k]))
#             if excluded_letter not in combination_str:
#                 combinations.append(combination_str)
#
# print(f"{' '.join(combinations)} {len(combinations)}")
# print(len(combinations))

first_letter = input()
second_letter = input()
third_letter = input()
x1 = 0
x2 = 0
x3 = 0
sum_of_valid = 0
for x1 in range(ord(first_letter), ord(second_letter) + 1):
    for x2 in range(ord(first_letter), ord(second_letter) + 1):
        for x3 in range(ord(first_letter), ord(second_letter) + 1):
            if x1 != ord(third_letter) and x2 != ord(third_letter) and x3 != ord(third_letter):
                sum_of_valid += 1
                print(f'{chr(x1)}{chr(x2)}{chr(x3)}', end=" ")

            else:
                continue
print(sum_of_valid)