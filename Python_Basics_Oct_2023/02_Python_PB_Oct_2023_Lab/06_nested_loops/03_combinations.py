#   x1 + x2 + x3 = n
result = int(input())
times = 0

for number_1 in range(0, result + 1):
    for number_2 in range(0, result + 1):
        for number_3 in range(0, result + 1):
            if number_1 + number_2 + number_3 == result:
                times += 1

print(times)
