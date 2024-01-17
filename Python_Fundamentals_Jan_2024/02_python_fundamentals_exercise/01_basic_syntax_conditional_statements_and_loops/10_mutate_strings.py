first_string = input()
second_string = input()

last_printed_string = first_string

for current_letter in range(len(first_string)):
    left_part = second_string[:current_letter+1]
    right_part = first_string[current_letter+1:]
    new_string = left_part + right_part
    if new_string == last_printed_string:
        continue
    else:
        last_printed_string = new_string
    print(new_string)
