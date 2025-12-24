from math import ceil

BRIOCHE_PRICE = 4
EGG_PRICE = 0.45

guests = int(input())
budget = int(input())

egg_number = guests * 2
brioche_number = ceil(guests / 3)

total_sum = BRIOCHE_PRICE * brioche_number + EGG_PRICE * egg_number

if budget >= total_sum:
    print(f"Lyubo bought {brioche_number} Easter bread and {egg_number} eggs.")
    money_left = budget - total_sum
    print(f"He has {money_left:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    money_needed = total_sum - budget
    print(f"He needs {money_needed:.2f} lv. more.")
