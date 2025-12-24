from math import floor,ceil

X = int(input())
Y = float(input())
Z = int(input())
worker_number = int(input())

total_grapes = X * Y
wine = 0.40 * total_grapes / 2.5

if wine < Z:
    diff = Z - wine
    print(f"It will be a tough winter! More {(floor(diff))} liters wine needed.")
else:
    diff = wine - Z
    liters_per_person = diff / worker_number
    print(f"Good harvest this year! Total wine: {(floor(wine))} liters.")
    print(f"{(ceil(diff))} liters left -> {(ceil(liters_per_person))} liters per person.")