total_sum = 0

days = int(input())
hours = int(input())

for day in range(1, days + 1):
    daily_sum = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0:
            if hour % 2 != 0:
                total_sum += 2.50
                daily_sum += 2.50
            else:
                total_sum += 1
                daily_sum += 1
        if day % 2 != 0:
            if hour % 2 == 0:
                total_sum += 1.25
                daily_sum += 1.25
            else:
                total_sum += 1
                daily_sum += 1
    print(f"Day: {day} - {daily_sum:.2f} leva")

print(f"Total: {total_sum:.2f} leva")