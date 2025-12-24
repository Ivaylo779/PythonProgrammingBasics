season = input()
kilometers_per_month = float(input())

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = kilometers_per_month * 0.75
        salary *= 4
    elif season == "Summer":
        salary = kilometers_per_month * 0.90
        salary *= 4
    elif season == "Winter":
        salary = kilometers_per_month * 1.05
        salary *= 4
if 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = kilometers_per_month * 0.95
        salary *= 4
    elif season == "Summer":
        salary = kilometers_per_month * 1.10
        salary *= 4
    elif season == "Winter":
        salary = kilometers_per_month * 1.25
        salary *= 4
if 10000 < kilometers_per_month <= 20000:
    salary = kilometers_per_month * 1.45
    salary *= 4

salary *= 0.90

print(f"{salary:.2f}")
