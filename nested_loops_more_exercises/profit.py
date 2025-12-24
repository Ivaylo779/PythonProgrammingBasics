one_lv_coins = int(input())
two_lv_coins = int(input())
five_lv_banknotes = int(input())
money_sum = int(input())

for x in range(one_lv_coins + 1):
    for y in range(two_lv_coins + 1):
        for z in range(five_lv_banknotes + 1):
            if x * 1 + y * 2 + z * 5 == money_sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {money_sum} lv.")



