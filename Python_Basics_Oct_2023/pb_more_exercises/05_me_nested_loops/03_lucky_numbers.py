number = int(input())
for happy_case in range(1_111, 10_000):
    happy_case_as_string = str(happy_case)
    # for index, digit in enumerate(happy_case_as_string):
    h_c_first = happy_case_as_string[0]
    h_c_second = happy_case_as_string[1]
    h_c_third = happy_case_as_string[2]
    h_c_forth = happy_case_as_string[3]
    if int(h_c_first) > 0 and int(h_c_second) > 0 and int(h_c_third) > 0 and int(h_c_forth) > 0:
        if int(h_c_first) + int(h_c_second) == int(h_c_third) + int(h_c_forth):
            if number % (int(h_c_first) + int(h_c_second)) == 0:
                print(f"{h_c_first}{h_c_second}{h_c_third}{h_c_forth}", end=" ")

