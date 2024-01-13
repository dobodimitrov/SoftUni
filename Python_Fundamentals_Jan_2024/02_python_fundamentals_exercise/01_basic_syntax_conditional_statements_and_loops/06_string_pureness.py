number = int(input())
char_1 = ","
char_2 = "."
char_3 = "_"

for number_of_strings in range(number):
    current_string = input()
    for char in current_string:
        if char == char_1 or char == char_2 or char == char_3:
            print(f"{current_string} is not pure!")
            break
    else:
        print(f"{current_string} is pure.")