n = int(input())
total_beer_quantity = 0
degrees_sum = 0

for _ in range(n):
    beer_quantity = float(input())
    beer_degree = float(input())
    total_beer_quantity += beer_quantity
    total_degrees = beer_quantity * beer_degree
    degrees_sum += total_degrees

average_value = degrees_sum / total_beer_quantity

print(f"Liter: {total_beer_quantity:.2f}")
print(f"Degrees: {average_value:.2f}")

if average_value < 38:
    print("Not good, you should baking!")
elif 38 <= average_value <42:
    print("Super!")
else:
    print("Dilution with distilled water!")