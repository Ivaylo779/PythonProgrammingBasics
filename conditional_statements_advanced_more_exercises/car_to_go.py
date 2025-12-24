budget = float(input())
season = input()

if budget <= 100:
    class_ride = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.65
if 100 < budget <= 500:
    class_ride = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.80
if budget > 500:
    class_ride = "Luxury class"
    if season == "Summer":
        car_type = "Jeep"
        price = budget * 0.90
    elif season == "Winter":
        car_type = "Jeep"
        price = budget * 0.90

print(class_ride)
print(f"{car_type} - {price:.2f}")

