guests = int(input())
cover_charge = float(input())
budget = float(input())

if 10 <= guests <= 15:
    cover_charge -= cover_charge * 0.15
elif 15 < guests <= 20:
    cover_charge -= cover_charge * 0.20
elif 20 < guests:
    cover_charge -= cover_charge * 0.25

cake_price = budget * 0.10

total_sum = cover_charge * guests + cake_price

if total_sum <= budget:
    diff = budget - total_sum
    print(f"It is party time! {diff:.2f} leva left.")
else:
    diff = total_sum - budget
    print(f"No party! {diff:.2f} leva needed.")
