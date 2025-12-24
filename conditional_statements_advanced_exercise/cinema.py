projection_type = input()
rows = int(input())
columns = int(input())

premiere = 12.00
normal = 7.50
discount = 5.00

if projection_type == "Premiere":
    total_sum = premiere * rows * columns
elif projection_type == "Normal":
    total_sum = normal * rows * columns
elif projection_type == "Discount":
    total_sum = discount * rows * columns

print(f"{total_sum:.2f}")




