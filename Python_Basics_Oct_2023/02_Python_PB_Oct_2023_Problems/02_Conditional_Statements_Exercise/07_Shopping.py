budget = float(input())
video_card_quantity = int(input())
processor_quantity = int(input())
memory_quantity = int(input())

video_card_price = 250
video_card_total = video_card_price * video_card_quantity
processor_price = 0.35 * video_card_total
processor_total = processor_price * processor_quantity
memory_price = 0.1 * video_card_total
memory_total = memory_price * memory_quantity

total_price = video_card_total + processor_total + memory_total
if video_card_quantity > processor_quantity:
    total_price *= 0.85

money_needed_or_left = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {money_needed_or_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {money_needed_or_left:.2f} leva more!')

