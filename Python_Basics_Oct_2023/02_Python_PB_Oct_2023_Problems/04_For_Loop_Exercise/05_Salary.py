number_of_websites = int(input())
salary = int(input())

for checking in range(1, number_of_websites + 1):
    name_of_website = input()
    if name_of_website == "Facebook":
        salary -= 150
    elif name_of_website == "Instagram":
        salary -= 100
    elif name_of_website == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(f'{salary}')
    