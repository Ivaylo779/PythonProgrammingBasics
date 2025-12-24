weight = float(input())
service_type = input()
distance = int(input())

surcharge_rate = 0
price_per_km = 0

if weight < 1:
    price_per_km = 0.03
    surcharge_rate = 0.80
elif weight < 10:
    price_per_km = 0.05
    surcharge_rate = 0.40
elif weight < 40:
    price_per_km = 0.10
    surcharge_rate = 0.05
elif weight < 90:
    price_per_km = 0.15
    surcharge_rate = 0.02
elif weight <= 150:
    price_per_km = 0.20
    surcharge_rate = 0.01

base_price = price_per_km * distance

if service_type == "express":
    surcharge = price_per_km * surcharge_rate * weight * distance
    total_price = base_price + surcharge
else:
    total_price = base_price

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
