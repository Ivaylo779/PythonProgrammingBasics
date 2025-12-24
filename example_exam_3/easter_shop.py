initial_eggs = int(input())
eggs_bought = 0

while True:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_bought} eggs sold.")
        break
    egg_number = int(input())
    if egg_number > initial_eggs and command == "Buy":
        print("Not enough eggs in store!")
        print(f"You can buy only {initial_eggs}.")
        break
    if command == "Buy":
        initial_eggs -= egg_number
        eggs_bought += egg_number
    else:
        initial_eggs += egg_number