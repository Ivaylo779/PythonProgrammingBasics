budget= float(input())

count = 0
product_price = 0
total_price = 0

while True:
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {count} products for {total_price:.2f} leva.")
        break
    count += 1
    product_price = float(input())
    if count % 3 == 0:
        product_price *= 0.50
    if product_price > budget:
        print("You don't have enough money!")
        missing_money = product_price - budget
        print(f"You need {missing_money:.2f} leva!")
        break
    budget -= product_price
    total_price += product_price


