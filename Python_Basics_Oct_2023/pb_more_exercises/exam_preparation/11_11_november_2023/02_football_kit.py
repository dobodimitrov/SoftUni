t_shirt_price = float(input())
sum_needed = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = 2 * (t_shirt_price + shorts_price)

total_sum = t_shirt_price + shorts_price + socks_price + shoes_price
total_after_discount = total_sum * 0.85      # 15% discount

if total_after_discount >= sum_needed:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_after_discount:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_needed - total_after_discount:.2f} lv. more.")
