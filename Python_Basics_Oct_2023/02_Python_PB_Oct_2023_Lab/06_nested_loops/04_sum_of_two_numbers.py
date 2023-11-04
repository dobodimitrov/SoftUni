number_1 = int(input())
number_2 = int(input())
result = int(input())
combination_counter = 0
combination_is_found = False

for first in range(number_1, number_2 + 1):
    for second in range(number_1, number_2 + 1):
        combination_counter += 1
        if first + second == result:
            combination_is_found = True
            break
    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{combination_counter} ({first} + {second} = {result})")
else:
    print(f"{combination_counter} combinations - neither equals {result}")
