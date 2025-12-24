budget = float(input())
series = int(input())
price = 0

for _ in range(series):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        price += series_price * 0.50
    elif series_name == "Lucifer":
        price += series_price * 0.60
    elif series_name == "Protector":
        price += series_price * 0.70
    elif series_name == "TotalDrama":
        price += series_price * 0.80
    elif series_name == "Area":
        price += series_price * 0.90
    else:
        price += series_price

if budget >= price:
    remaining_money = budget - price
    print(f"You bought all the series and left with {remaining_money:.2f} lv.")
else:
    needed_money = price - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")