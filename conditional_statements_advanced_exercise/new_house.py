flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
discount = 0

if flower_type == "Roses":
    price = 5
    if number_of_flowers > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    price = 3.80
    if number_of_flowers > 90:
        discount = 0.15
elif flower_type == "Tulips":
    price = 2.80
    if number_of_flowers > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = 2.50
    if number_of_flowers < 80:
        price += price * 0.20

total_sum = price * number_of_flowers
total_sum -= total_sum * discount

if budget >= total_sum:
    remaining_money = budget - total_sum
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {remaining_money:.2f} leva left.")
else:
    needed_money = total_sum - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")