dog_food = int(input())
food_in_grams = dog_food * 1000
food_eaten = 0

while True:
    command = input()
    if command == "Adopted":
        break
    command = int(command)
    food_eaten += command

if food_in_grams >= food_eaten:
    diff = food_in_grams - food_eaten
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    diff = food_eaten - food_in_grams
    print(f"Food is not enough. You need {diff} grams more." )