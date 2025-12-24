budget = float(input())
fuel_needed = float(input())
week_day = input()

fuel_price = fuel_needed * 2.10

total_price = fuel_price + 100

if week_day == "Saturday":
    total_price *= 0.90
elif week_day == "Sunday":
    total_price *= 0.80

if budget >= total_price:
    money_left = budget - total_price
    print(f"Safari time! Money left: {money_left:.2f} lv. ")
else:
    missing_money = total_price - budget
    print(f"Not enough money! Money needed: {missing_money:.2f} lv.")