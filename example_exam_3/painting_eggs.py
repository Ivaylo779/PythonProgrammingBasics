egg_size = input()
egg_color = input()
batches = int(input())

if egg_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    elif egg_color == "Yellow":
        price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    elif egg_color == "Yellow":
        price = 7
elif egg_size == "Small":
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    elif egg_color == "Yellow":
        price = 5

total_sum = batches * price
total_sum -= (total_sum * 0.35)

print(f"{total_sum:.2f} leva.")