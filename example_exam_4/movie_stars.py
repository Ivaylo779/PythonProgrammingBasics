budget = float(input())

while True:
    actor_name = input()
    if actor_name == "ACTION":
        break
    if len(actor_name) <= 15:
        salary = float(input())
        budget -= salary
    else:
        salary = budget * 0.20
        budget -= salary
    if budget < 0:
        break

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")