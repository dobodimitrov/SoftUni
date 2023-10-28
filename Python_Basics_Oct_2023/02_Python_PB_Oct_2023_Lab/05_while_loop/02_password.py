username = input()
password = input()
login_password = input()
while password != login_password:
    login_password = input()

print(f"Welcome {username}!")
