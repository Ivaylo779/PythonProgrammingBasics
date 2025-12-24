cargo_number = int(input())
minibus_tonnage = 0
truck_tonnage = 0
train_tonnage = 0
total_tons = 0
average_price = 0

for _ in range(1, cargo_number + 1):
    tonnage = int(input())
    if 0 < tonnage <= 3:
        price_per_ton = 200
        minibus_tonnage += tonnage
    elif 3 < tonnage <= 11:
        price_per_ton = 175
        truck_tonnage += tonnage
    elif 11 < tonnage:
        price_per_ton = 120
        train_tonnage += tonnage

    total_tons += tonnage

    average_price += tonnage * price_per_ton

average_price /= total_tons
print(f"{average_price:.2f}")
minibus_percentage = minibus_tonnage / total_tons * 100
print(f"{minibus_percentage:.2f}%")
truck_percentage = truck_tonnage / total_tons * 100
print(f"{truck_percentage:.2f}%")
train_percentage = train_tonnage / total_tons * 100
print(f"{train_percentage:.2f}%")