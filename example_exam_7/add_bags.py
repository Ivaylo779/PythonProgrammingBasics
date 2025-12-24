above_20_kg_price = float(input())
baggage_kgs = float(input())
days_until_trip = int(input())
baggage_number = int(input())

if baggage_kgs < 10:
    price = above_20_kg_price * 0.20
elif 10 <= baggage_kgs <= 20:
    price = above_20_kg_price * 0.50
else:
    price = above_20_kg_price

if days_until_trip > 30:
    price *= 1.10
elif 7 <= days_until_trip <= 30:
    price *= 1.15
else:
    price *= 1.40

price *= baggage_number

print(f" The total price of bags is: {price:.2f} lv. ")
