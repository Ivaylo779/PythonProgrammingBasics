name = input()
password = input()
passcode = input()

while password != passcode:
    passcode = input()
print(f"Welcome {name}!")
