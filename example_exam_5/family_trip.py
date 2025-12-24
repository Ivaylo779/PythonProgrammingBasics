budget = float(input())
night_stays = int(input())
night_stay_price = float(input())
additional_expense_percentage = int(input())

if night_stays > 7:
    night_stay_price *= 0.95

total_stay_price = night_stays * night_stay_price
additional_expenses = (budget * additional_expense_percentage) / 100

total_sum = total_stay_price + additional_expenses

if total_sum > budget:
    money_needed = total_sum - budget
    print(f"{money_needed:.2f} leva needed.")
else:
    remaining_money = budget - total_sum
    print(f"Ivanovi will be left with {remaining_money:.2f} leva after vacation.")
