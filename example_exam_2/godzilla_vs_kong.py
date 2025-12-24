film_budget = float(input())
extras = int(input())
clothing_price = float(input())

decor = film_budget * 0.10

if extras > 150:
    clothing_price -= clothing_price * 0.10

clothing_sum = extras * clothing_price

total_sum = decor + clothing_sum

if total_sum > film_budget:
    diff = total_sum - film_budget
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    diff = film_budget - total_sum
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")