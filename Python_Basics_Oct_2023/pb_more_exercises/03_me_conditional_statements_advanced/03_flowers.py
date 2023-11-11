chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
bouquet_total = 0
discount = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00 * chrysanthemums_count
    roses_price = 4.10 * roses_count
    tulips_price = 2.50 * tulips_count
    if tulips_count > 7:
        discount += 0.05
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75 * chrysanthemums_count
    roses_price = 4.50 * roses_count
    tulips_price = 4.15 * tulips_count
    if season == "Winter" and roses_count >= 10:
        discount += 0.1

bouquet_total += chrysanthemums_price + roses_price + tulips_price
if chrysanthemums_count + roses_count + tulips_count > 20:
    bouquet_total *= 0.8

if holiday == "Y":
    bouquet_total *= 1.15

bouquet_total -= bouquet_total * discount
bouquet_total += 2
print(f"{bouquet_total:.2f}")





# В празнични дни цените на всички цветя се увеличават с 15%. Предлагат се следните отстъпки:
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
