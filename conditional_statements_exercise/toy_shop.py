PUZZLE = 2.60
DOLL = 3
BEAR = 4.10
MINION = 8.20
TRUCK = 2

vacation_price = float(input())
puzzle_amount = int(input())
doll_amount = int(input())
bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

total_sum = (puzzle_amount * PUZZLE + doll_amount * DOLL + bear_amount * BEAR
             + minion_amount * MINION + truck_amount * TRUCK)

ordered_toys = puzzle_amount + doll_amount + bear_amount + minion_amount + truck_amount

if ordered_toys >= 50:
    discount_amount = total_sum * 0.25
    total_sum = total_sum - discount_amount

final_price = total_sum - (total_sum * 0.10)

if final_price >= vacation_price:
    change = final_price - vacation_price
    print(f"Yes! {change:.02f} lv left.")
elif final_price < vacation_price:
    not_enough = vacation_price - final_price
    print(f"Not enough money! {not_enough:.02f} lv needed.")