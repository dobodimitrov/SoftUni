CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menu_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())

total_menu_prices = chicken_menu_quantity * CHICKEN_MENU_PRICE + fish_menu_quantity * FISH_MENU_PRICE +vegetarian_menu_quantity * VEGETARIAN_MENU_PRICE
desert_price = 0.2 * total_menu_prices
total_bill = total_menu_prices + desert_price + DELIVERY_PRICE

print(total_bill)