tourney_days = int(input())

charity_money = 0
total_wins = 0
total_losses = 0

for _ in range(tourney_days):
    wins = 0
    losses = 0
    raised_money = 0
    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            wins += 1
            raised_money += 20
        else:
            losses += 1
    if wins > losses:
        raised_money *= 1.10
        total_wins += 1
    else:
        total_losses += 1

    charity_money += raised_money

if total_wins > total_losses:
    charity_money *= 1.20
    print(f"You won the tournament! Total raised money: {charity_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {charity_money:.2f}")

