bought_dog_food = int(input())
bought_dog_food *= 1000

total_food_eaten = 0

while True:
    command = input()
    if command == "Adopted":
        break
    dog_food_eaten = int(command)
    total_food_eaten += dog_food_eaten

if bought_dog_food >= total_food_eaten:
    leftover_dog_food = bought_dog_food - total_food_eaten
    print(f"Food is enough! Leftovers: {leftover_dog_food} grams.")
else:
    dog_food_needed = total_food_eaten - bought_dog_food
    print(f"Food is not enough. You need {dog_food_needed} grams more." )

