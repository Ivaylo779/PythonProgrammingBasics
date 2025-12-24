BITCOIN = 1168
YUAN = 0.15
DOLLAR = 1.76
EURO = 1.95

bitcoin_number = int(input())
yuan_number = float(input())
commission_fee = float(input())

in_leva = (YUAN * yuan_number) * 1.76

total_sum = bitcoin_number * BITCOIN + in_leva
total_sum /= EURO
total_sum -= commission_fee * total_sum / 100

print(f"{total_sum:.2f}")