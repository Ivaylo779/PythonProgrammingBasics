season = input()
group_type = input()
students = int(input())
overnight_stays = int(input())

if group_type == "girls":
    if season == "Winter":
        price = 9.60
        sport = "Gymnastics"
    elif season == "Spring":
        price = 7.20
        sport = "Athletics"
    elif season == "Summer":
        price = 15
        sport = "Volleyball"

elif group_type == "boys":
    if season == "Winter":
        price = 9.60
        sport = "Judo"
    elif season == "Spring":
        price = 7.20
        sport = "Tennis"
    elif season == "Summer":
        price = 15
        sport = "Football"

elif group_type == "mixed":
    if season == "Winter":
        price = 10
        sport = "Ski"
    elif season == "Spring":
        price = 9.50
        sport = "Cycling"
    elif season == "Summer":
        price = 20
        sport = "Swimming"

price *= students * overnight_stays

if 10 <= students < 20:
    price -= price * 0.05
elif 20 <= students < 50:
    price -= price * 0.15
elif 50 <= students:
    price -= price * 0.50

print(f"{sport} {price:.2f} lv.")




