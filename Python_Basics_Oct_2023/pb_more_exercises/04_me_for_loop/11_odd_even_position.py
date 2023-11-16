import sys

count_of_numbers = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for sequence in range(1, count_of_numbers + 1):
    current_number = float(input())
    if sequence % 2 == 1:       # is odd
        odd_sum += current_number
        if count_of_numbers != 0:
            if current_number > odd_max:
                odd_max = current_number
            if current_number < odd_min:
                odd_min = current_number
    if sequence % 2 == 0:     # is even
        even_sum += current_number
        if count_of_numbers > 1:
            if current_number > even_max:
                even_max = current_number
            if current_number < even_min:
                even_min = current_number

print(f"OddSum={odd_sum:.2f},")
if odd_min != sys.maxsize:
    print(f"OddMin={odd_min:.2f},")
else:
    print("OddMin=No,")

if odd_max != -sys.maxsize:
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMax=No,")

print(f"EvenSum={even_sum:.2f},")
if even_min != sys.maxsize:
    print(f"EvenMin={even_min:.2f},")
else:
    print("EvenMin=No,")
if even_max != -sys.maxsize:
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMax=No")
