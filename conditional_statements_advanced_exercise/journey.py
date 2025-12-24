budget = float(input())
season = input()
price = 0
destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
    elif season == "winter":
        price = budget * 0.70
elif  100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
    elif season == "winter":
        price = budget * 0.80
else:
    destination = "Europe"
    if season == "summer" or season == "winter":
        price = budget * 0.90

if season == "summer":
    place = "Camp"
elif season == "winter":
    place = "Hotel"

if destination == "Europe":
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")

