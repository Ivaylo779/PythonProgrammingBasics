championship_stage = input()
ticket_type = input()
ticket_number = int(input())
picture = input()

if championship_stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif championship_stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif championship_stage == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400

price = ticket_number * price
picture_price = 40

if price > 4000:
    price -= price * 0.25
elif price > 2500:
    price -= price * 0.10
    if picture == "Y":
        price += ticket_number * picture_price
else:
    if picture == "Y":
        price += ticket_number * picture_price

print(f"{price:.2f}")
