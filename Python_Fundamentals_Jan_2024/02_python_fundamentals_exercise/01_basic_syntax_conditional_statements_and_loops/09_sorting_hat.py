command = input()
is_successful = True
while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        is_successful = False
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()

if is_successful:
    print("Welcome to Hogwarts.")