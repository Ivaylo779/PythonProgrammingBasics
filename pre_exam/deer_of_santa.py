from math import floor,ceil

days_absent = int(input())
food_left = int(input())
food_per_day_deer1 = float(input())
food_per_day_deer2 = float(input())
food_per_day_deer3 = float(input())

deer1_food = days_absent * food_per_day_deer1
deer2_food = days_absent * food_per_day_deer2
deer3_food = days_absent * food_per_day_deer3

total_food = deer1_food + deer2_food + deer3_food

if total_food < food_left:
    diff = food_left - total_food
    print(f"{(floor(diff))} kilos of food left.")
else:
    diff = total_food - food_left
    print(f"{(ceil(diff))} more kilos of food are needed.")
