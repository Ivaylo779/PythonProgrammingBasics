w = float(input())
h = float(input())

w_cm = w * 100
h_cm = h * 100

columns = int((h_cm - 100) // 70)
rows = int(w_cm // 120)

total_seats = rows * columns - 3

print(total_seats)
