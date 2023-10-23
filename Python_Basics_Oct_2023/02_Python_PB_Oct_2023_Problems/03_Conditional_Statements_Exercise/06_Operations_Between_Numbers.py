# · N1 - цяло число;
# · N2 - цяло число;
# · Оператор - един символ измежду: "+", "-", "*", "/", "%

number_1 = int(input())
number_2 = int(input())
operator = input()

if operator == "+":
    if (number_1 + number_2) % 2 == 0:
        print(f"{number_1} + {number_2} = {number_1 + number_2} - even")
    else:
        print(f"{number_1} + {number_2} = {number_1 + number_2} - odd")
elif operator == "-":
    if (number_1 - number_2) % 2 == 0:
        print(f"{number_1} - {number_2} = {number_1 - number_2} - even")
    else:
        print(f"{number_1} - {number_2} = {number_1 - number_2} - odd")
elif operator == "*":
    if (number_1 * number_2) % 2 == 0:
        print(f"{number_1} * {number_2} = {number_1 * number_2} - even")
    else:
        print(f"{number_1} * {number_2} = {number_1 * number_2} - odd")
elif operator == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} / {number_2} = {(number_1 / number_2):.2f}")
elif operator == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} % {number_2} = {number_1 % number_2}")



# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата
# и дали той е четен или нечетен.При обикновеното деление - резултата.При модулното деление - остатъка.