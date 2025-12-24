needed_money = float(input())
owned_money = float(input())

spending_counter = 0
days = 0

while True:
    days += 1
    action_type = input()
    money = float(input())

    if action_type == "spend":
        spending_counter += 1
        if money > owned_money:
            owned_money = 0
        else:
            owned_money -= money
    elif action_type == "save":
        owned_money += money
        spending_counter = 0

    if spending_counter == 5:
        print("You can't save the money.")
        print(days)
        break

    if owned_money >= needed_money:
        print(f"You saved the money for {days} days.")
        break
