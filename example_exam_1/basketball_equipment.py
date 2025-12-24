annual_tax = int(input())

sneakers_price = annual_tax - (annual_tax * 0.40)
equipment_price = sneakers_price - (sneakers_price * 0.20)
ball_price = equipment_price * 1/4
accessories_price = ball_price * 1/5

total_sum = annual_tax + sneakers_price + equipment_price + ball_price + accessories_price

print(f"{total_sum:.2f}")