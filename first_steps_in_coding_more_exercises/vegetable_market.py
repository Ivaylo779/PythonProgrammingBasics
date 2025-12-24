vegetable_price = float(input())
fruit_price = float(input())
total_vegetables = int(input())
total_fruits = int(input())

total_sum = total_vegetables * vegetable_price + total_fruits * fruit_price
in_euro = total_sum / 1.94

print(f"{in_euro:.2f}")

