n = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toys = 0
money_gift = 0

for year in range(1, n + 1):
    if year % 2 == 0:
        money_gift += 10.00
        money += money_gift - 1
    else:
        toys += 1

toy_reward = toys * toy_price
total_sum = toy_reward + money

if total_sum >= washing_machine_price:
    leftover_sum = total_sum - washing_machine_price
    print(f"Yes! {leftover_sum:.2f}")
else:
    diff = washing_machine_price - total_sum
    print(f"No! {diff:.2f}")