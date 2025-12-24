hours = int(input())
minutes = int(input())

total_minutes = hours * 60 + minutes
total_minutes += 15

new_hour = total_minutes // 60
new_minutes = total_minutes % 60

if new_hour == 24:
    new_hour = 0

print(f"{new_hour}:{new_minutes:02d}")