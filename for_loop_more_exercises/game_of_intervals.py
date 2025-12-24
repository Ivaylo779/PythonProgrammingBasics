move_count = int(input())
score = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_nums = 0

for num in range(1, move_count + 1):
    move = int(input())
    if 0 <= move <= 9:
        score += move * 0.20
        from_0_to_9 += 1
    elif 10 <= move <= 19:
        score += move * 0.30
        from_10_to_19 += 1
    elif 20 <= move <= 29:
        score += move * 0.40
        from_20_to_29 += 1
    elif 30 <= move <= 39:
        score += 50
        from_30_to_39 += 1
    elif 40 <= move <= 50:
        score += 100
        from_40_to_50 += 1
    else:
        score /= 2
        invalid_nums += 1

percentage_1 = (from_0_to_9 / move_count) * 100
percentage_2 = (from_10_to_19 / move_count) * 100
percentage_3 = (from_20_to_29 / move_count) * 100
percentage_4 = (from_30_to_39 / move_count) * 100
percentage_5 = (from_40_to_50 / move_count) * 100
percentage_6 = (invalid_nums / move_count) * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {percentage_1:.2f}%")
print(f"From 10 to 19: {percentage_2:.2f}%")
print(f"From 20 to 29: {percentage_3:.2f}%" )
print(f"From 30 to 39: {percentage_4:.2f}%")
print(f"From 40 to 50: {percentage_5:.2f}%")
print(f"Invalid numbers: {percentage_6:.2f}%")

