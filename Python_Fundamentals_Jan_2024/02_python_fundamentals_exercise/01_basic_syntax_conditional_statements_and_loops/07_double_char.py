command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
    for char in command:
        print(char * 2, end="")
    print()
    command = input()