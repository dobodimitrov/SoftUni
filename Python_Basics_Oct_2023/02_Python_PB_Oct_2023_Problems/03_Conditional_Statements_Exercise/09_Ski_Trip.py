room_for_one = 18.00
apartment = 25.00
president_apartment = 35.00

days_stay = int(input()) - 1
type_of_room = input()
rating = input()
price_total = 0

if type_of_room == "room for one person":
    price_total = room_for_one * days_stay
elif type_of_room == "apartment":
    if days_stay < 10:
        price_total = 0.7 * (apartment * days_stay)
    elif 10 <= days_stay <= 15:
        price_total = 0.65 * (apartment * days_stay)
    elif days_stay > 15:
        price_total = 0.5 * (apartment * days_stay)
elif type_of_room == "president apartment":
    if days_stay < 10:
        price_total = 0.9 * (president_apartment * days_stay)
    elif 10 <= days_stay <= 15:
        price_total = 0.85 * (president_apartment * days_stay)
    elif days_stay > 15:
        price_total = 0.8 * (president_apartment * days_stay)

if rating == "positive":
    price_total *= 1.25
    print(f'{price_total:.2f}')
if rating == "negative":
    price_total *= 0.9
    print(f'{price_total:.2f}')
