film_budget = float(input())
number_of_extras = int(input())
clothing = float(input())

decor = film_budget * 0.10

if number_of_extras > 150:
    clothing = clothing - (clothing * 0.10)

price_for_extras = number_of_extras * clothing
final_price = price_for_extras + decor

if final_price > film_budget:
    not_enough = final_price - film_budget
    print("Not enough money!")
    print(f"Wingard needs {not_enough:.2f} leva more.")
elif final_price <= film_budget:
    change = film_budget - final_price
    print("Action!")
    print(f"Wingard starts filming with {change:.2f} leva left.")