n = int(input())
sum = 0

for _ in range(n):
    numbers = int(input())
    sum += numbers

average = sum / n

print(f"{average:.2f}")