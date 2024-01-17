# year = int(input())
#
# while True:
#     year += 1
#     is_happy_year = True
#     already_found_digits = ""
#     for digit in str(year):
#         if digit in already_found_digits:
#             is_happy_year = False
#         already_found_digits += digit
#     if is_happy_year:
#         break
# print(year)
#
#
year = int(input())
is_happy_year = True
while True:
    year += 1
    if len(str(year)) == len(set(str(year))):
        break

print(year)
