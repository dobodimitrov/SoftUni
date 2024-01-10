number = int(input())

for i in range(number + 1):
    for j in range(i):
        print("*", end="")
    print()

for u in range(number - 1, 0, -1):
    for v in range(u):
        print("*", end="")
    print()