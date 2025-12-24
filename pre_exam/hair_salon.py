command = ""
money = 0
income = 0

daily_goal = int(input())

while True:
    command = input()
    if command == "closed":
        break
    if command == "haircut":
        type = input()
        if type == "mens":
            income = 15
        elif type == "ladies":
            income = 20
        elif type == "kids":
            income = 10
    if command == "color":
        type = input()
        if type == "touch up":
            income = 20
        elif type == "full color":
            income = 30
    money += income
    if money >= daily_goal:
        break

if money >= daily_goal:
    print("You have reached your target for the day!" )
    print(f"Earned money: {money}lv.")
else:
    diff = daily_goal - money
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {money}lv.")