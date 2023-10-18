projection_type = input()
number_of_rows = int(input())
number_of_columns = int(input())
income = 0

total_seats = number_of_columns * number_of_rows

if projection_type == "Premiere":
    income = total_seats * 12.00
    print(f'{income:.2f} leva')
elif projection_type == "Normal":
    income = total_seats * 7.50
    print(f'{income:.2f} leva')
elif projection_type == "Discount":
    income = total_seats * 5.00
    print(f'{income:.2f} leva')