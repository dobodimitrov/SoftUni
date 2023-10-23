# · Бюджет - реално число;
# · Един от двата възможни сезона - "summer” или "winter”.

budget = float(input())
season = input()
destination = ""
type_of_accommodation = ""
price_of_accommodation = 0
money_spent = 0

if season == "summer":
    type_of_accommodation = "Camp"
elif season == "winter":
    type_of_accommodation = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = 0.3 * budget
    elif season == "winter":
        money_spent = 0.7 * budget
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = 0.4 * budget
    elif season == "winter":
        money_spent = 0.8 * budget
elif 1000 < budget:
    destination = "Europe"
    type_of_accommodation = "Hotel"
    money_spent = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{type_of_accommodation} - {money_spent:.2f}")

# При 100 лв. или по-малко - някъде в България:
# o Лято - 30% от бюджета;
# o Зима - 70% от бюджета.
# · При 1000 лв. или по малко - някъде на Балканите:
# o Лято - 40% от бюджета;
# o Зима - 80% от бюджета.
# · При повече от 1000 лв. - някъде из Европа:
# o При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.




# Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел