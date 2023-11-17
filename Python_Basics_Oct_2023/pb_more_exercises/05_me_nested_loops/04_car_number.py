down_limit = int(input())
upper_limit = int(input())

for number in range(1_000, 10_000):
    number_as_string = str(number)
    num_first = number_as_string[0]
    num_second = number_as_string[1]
    num_third = number_as_string[2]
    num_forth = number_as_string[3]
    if down_limit <= int(num_first) <= upper_limit and \
            down_limit <= int(num_second) <= upper_limit and \
            down_limit <= int(num_third) <= upper_limit and \
            down_limit <= int(num_forth) <= upper_limit:
        if int(num_first) % 2 == 0 and int(num_forth) % 2 == 1 or \
                int(num_first) % 2 == 1 and int(num_forth) % 2 == 0:
            if int(num_first) > int(num_forth):
                if (int(num_second) + int(num_third)) % 2 == 0:
                    print(f"{num_first}{num_second}{num_third}{num_forth}", end=" ")