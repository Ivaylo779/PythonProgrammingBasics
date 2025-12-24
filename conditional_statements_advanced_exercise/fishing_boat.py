budget = int(input())
season = input()
fishermen = int(input())
price = 0
discount = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fishermen <= 6:
    discount = 0.10
elif 7 < fishermen <= 11:
    discount = 0.15
else:
    discount = 0.25

total_sum = price
total_sum -= total_sum * discount

if fishermen % 2 == 0 and season != "Autumn":
    total_sum -= total_sum * 0.05

if budget >= total_sum:
    remaining_money = budget - total_sum
    print(f"Yes! You have {remaining_money:.2f} leva left.")
else:
    needed_money = total_sum - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
