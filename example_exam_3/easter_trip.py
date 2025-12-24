destination = input()
reservation_date = input()
night_stays = int(input())

if destination == "France":
    if reservation_date == "21-23":
        price = 30
    elif reservation_date == "24-27":
        price = 35
    elif reservation_date == "28-31":
        price = 40
elif destination == "Italy":
    if reservation_date == "21-23":
        price = 28
    elif reservation_date == "24-27":
        price = 32
    elif reservation_date == "28-31":
        price = 39
elif destination == "Germany":
    if reservation_date == "21-23":
        price = 32
    elif reservation_date == "24-27":
        price = 37
    elif reservation_date == "28-31":
        price = 43

total_price = price * night_stays

print(f"Easter trip to {destination} : {total_price:.2f} leva.")