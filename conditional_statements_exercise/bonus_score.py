points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points += 5

elif  100 < points <= 1000:
    bonus_points = points * 0.20

else:
    bonus_points = points * 0.10

if points % 2 == 0:
    bonus_points += 1

elif points % 5== 0:
   bonus_points += 2

total_points = points + bonus_points

print(f"{bonus_points:.1f}")
print(f"{total_points:.1f}")


