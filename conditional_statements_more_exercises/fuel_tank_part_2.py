fuel_type = input()
fuel_quantity = float(input())
club_card = input()
price = 0

if fuel_type == "Gasoline":
    price = fuel_quantity * 2.22
    if club_card == "Yes":
        price -= fuel_quantity * 0.18
elif fuel_type == "Diesel":
    price = fuel_quantity * 2.33
    if club_card == "Yes":
        price -= fuel_quantity * 0.12
elif fuel_type == "Gas":
    price = fuel_quantity * 0.93
    if club_card == "Yes":
        price -= fuel_quantity * 0.08

if 20 <= fuel_quantity <= 25:
    price -= price * 0.08
elif fuel_quantity > 25:
    price -= price * 0.10


print(f"{price:.2f} lv." )