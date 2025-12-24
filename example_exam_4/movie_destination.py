budget = float(input())
destination = input()
season = input()
days = int(input())

if season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20250
elif season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000

total_price = price * days

if destination == "Dubai":
    total_price *= 0.70
elif destination == "Sofia":
    total_price += total_price * 0.25

if total_price <= budget:
    diff = budget - total_price
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    diff = total_price - budget
    print(f"The director needs {diff:.2f} leva more!")