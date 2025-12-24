month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights > 14:
        studio -= studio * 0.30
    elif nights > 7:
        studio -= studio * 0.05
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio -= studio * 0.20
elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if nights > 14:
    apartment -= apartment * 0.10

total_studio = studio * nights
total_apartment = apartment * nights

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
