number = float(input())

if number == 0:
    print(f"zero")
elif abs(number) < 1:
    print(f"small", end=" ")
elif abs(number) > 1_000_000:
    print(f"large", end=" ")

if number > 0:
    print(f"positive")
elif number < 0:
    print(f"negative")