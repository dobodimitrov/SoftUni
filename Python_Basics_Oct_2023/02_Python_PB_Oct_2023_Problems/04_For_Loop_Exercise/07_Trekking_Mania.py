count_of_groups = int(input())
musalla = 0  # <= 5
mont_blanc = 0    # 6 - 12
kilimanjaro = 0    # 13 - 25
k2 = 0    # 26 - 40
everest = 0    # > 41
total_number_of_people = 0

for teams in range(1, count_of_groups + 1):
    number_of_people = int(input())
    total_number_of_people += number_of_people
    if number_of_people <= 5:
        musalla += number_of_people
    elif 5 < number_of_people <= 12:
        mont_blanc += number_of_people
    elif 12 < number_of_people <= 25:
        kilimanjaro += number_of_people
    elif 25 < number_of_people <= 40:
        k2 += number_of_people
    else:
        everest += number_of_people

musalla_percentage = (musalla / total_number_of_people) * 100
mont_blanc_percentage = (mont_blanc / total_number_of_people) * 100
kilimanjaro_percentage = (kilimanjaro / total_number_of_people) * 100
k2_percentage = (k2 / total_number_of_people) * 100
everest_percentage = (everest / total_number_of_people) * 100

print(f'{musalla_percentage:.2f}%')
print(f'{mont_blanc_percentage:.2f}%')
print(f'{kilimanjaro_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')