num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
is_holiday = input()

if season == "Spring" or season == "Summer":
    chrysanthemums = 2.00
    roses = 4.10
    tulips = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums = 3.75
    roses = 4.50
    tulips = 4.15

price = chrysanthemums * num_chrysanthemums + roses * num_roses + tulips * num_tulips

if is_holiday == "Y":
    price += price * 0.15

if num_tulips > 7 and season == "Spring":
    price -= price * 0.05
if num_roses >= 10 and season == "Winter":
    price -= price * 0.10
if num_chrysanthemums + num_roses + num_tulips > 20:
    price -= price * 0.20

price += 2

print(f"{price:.2f}")