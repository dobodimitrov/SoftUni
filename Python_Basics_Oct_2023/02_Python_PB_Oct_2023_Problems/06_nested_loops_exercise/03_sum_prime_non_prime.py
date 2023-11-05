command = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0

while command != "stop":
    int_number = int(command)
    if int_number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for n in range(2, int_number):
        if int_number % n == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers_sum += int_number
    else:
        non_prime_numbers_sum += int_number
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
