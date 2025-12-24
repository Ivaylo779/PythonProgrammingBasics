desired_profit = float(input())

profit = 0

while profit < desired_profit:
    cocktail_name = input()
    if cocktail_name == "Party!":
        missing_sum = desired_profit - profit
        print(f"We need {missing_sum:.2f} leva more.")
        break
    cocktail_number = int(input())
    cocktail_price = len(cocktail_name)
    order = cocktail_price * cocktail_number
    if order % 2 != 0:
        order *= 0.75
    profit += order

else:
    print("Target acquired.")

print(f"Club income - {profit:.2f} leva.")