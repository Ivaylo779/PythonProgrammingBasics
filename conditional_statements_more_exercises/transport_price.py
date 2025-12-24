n = int(input())
travel = input()
price = 0

if travel == "day":
    if n < 20:
        price = 0.70 + n * 0.79
    elif n < 100:
        price = n * 0.09
    else:
        price = n * 0.06
else:
    if n < 20:
        price = 0.70 + n * 0.90
    elif n < 100:
        price = n * 0.09
    else:
        price = n * 0.06

print(f"{price:.2f}")
