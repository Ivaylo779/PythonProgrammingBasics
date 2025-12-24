budget = float(input())
category = input()
people_in_group = int(input())

if 1 <= people_in_group <= 4:
    budget = budget * 0.25
elif 5 <= people_in_group <= 9:
    budget = budget * 0.40
elif 10 <= people_in_group <= 24:
    budget = budget * 0.50
elif 25 <= people_in_group <= 49:
    budget = budget * 0.60
elif 50 <= people_in_group:
    budget = budget * 0.75

if category == "Normal":
    budget -= people_in_group * 249.99
elif category == "VIP":
    budget -= people_in_group * 499.99

if budget > 0:
    print(f"Yes! You have {budget:.2f} leva left." )
else:
    print(f"Not enough money! You need {abs(budget):.2f} leva." )