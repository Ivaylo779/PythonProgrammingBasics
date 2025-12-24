days = int(input())
total_food_quantity = float(input())

biscuit_quantity = 0
total_dog_food_eaten = 0
total_cat_food_eaten = 0

for day in range(1, days + 1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    total_dog_food_eaten += dog_food_eaten
    total_cat_food_eaten += cat_food_eaten
    if day % 3 == 0:
        total_food_eaten = dog_food_eaten + cat_food_eaten
        biscuit_quantity += total_food_eaten * 0.10


print(f"Total eaten biscuits: {round(biscuit_quantity)}gr.")
print(f"{((total_dog_food_eaten + total_cat_food_eaten) / total_food_quantity) * 100:.2f}% of the food has been eaten.")
print(f"{(total_dog_food_eaten / (total_dog_food_eaten + total_cat_food_eaten)) * 100:.2f}% eaten from the dog.")
print(f"{(total_cat_food_eaten / (total_dog_food_eaten + total_cat_food_eaten)) * 100:.2f}% eaten from the cat.")