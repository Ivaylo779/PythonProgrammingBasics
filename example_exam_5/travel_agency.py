city_name = input()
packet_type = input()
vip_discount = input()
days_staying = int(input())

price = 0

if city_name == "Bansko" or city_name == "Borovets":
    if packet_type == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price *= 0.90
    elif packet_type == "noEquipment":
        price = 80
        if vip_discount == "yes":
             price *= 0.95
elif city_name == "Varna" or city_name == "Burgas":
    if packet_type == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price *= 0.88
    elif packet_type == "noBreakfast":
        price = 100
        if vip_discount == "yes":
            price *= 0.93

if days_staying > 7:
    days_staying -= 1

total_price = price * days_staying

if ((city_name != "Varna" and city_name != "Burgas" and city_name != "Bansko" and city_name != "Borovets") or
    (packet_type != "noEquipment" and packet_type != "withEquipment" and
    packet_type != "noBreakfast" and packet_type != "withBreakfast")):
    print("Invalid input!")
elif days_staying < 1:
    print("Days must be positive number!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")


