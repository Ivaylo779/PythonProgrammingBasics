from math import ceil,floor

days = int(input())
food_left = int(input())
daily_dog_food = float(input())
daily_cat_food = float(input())
daily_turtle_food = float(input())

dog_food = days * daily_dog_food
cat_food = days * daily_cat_food
turtle_food = (days * daily_turtle_food) / 1000

total_food = dog_food + cat_food + turtle_food

if total_food < food_left:
    diff = food_left - total_food
    print(f"{(floor(diff))} kilos of food left.")
else:
    diff = total_food - food_left
    print(f"{(ceil(diff))} more kilos of food are needed.")
