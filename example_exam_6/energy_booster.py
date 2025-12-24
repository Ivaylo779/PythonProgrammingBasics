fruit_gel = input()
set_size = input()
set_number = int(input())

if set_size == "small":
    gel_number = 2
    if fruit_gel == "Watermelon":
        price = 56
    elif fruit_gel == "Mango":
        price = 36.66
    elif fruit_gel == "Pineapple":
        price = 42.10
    elif fruit_gel == "Raspberry":
        price = 20
elif set_size == "big":
    gel_number = 5
    if fruit_gel == "Watermelon":
        price = 28.70
    elif fruit_gel == "Mango":
        price = 19.60
    elif fruit_gel == "Pineapple":
        price = 24.80
    elif fruit_gel == "Raspberry":
        price = 15.20

total_price = (price * gel_number) * set_number

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")