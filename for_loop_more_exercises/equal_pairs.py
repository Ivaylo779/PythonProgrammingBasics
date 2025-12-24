n = int(input())

max_diff = 0

a = int(input())
b = int(input())
prev_sum = a + b

for _ in range(n - 1):
    a = int(input())
    b = int(input())
    current_sum = a + b
    diff = abs(current_sum - prev_sum)
    if diff > max_diff:
        max_diff = diff
    prev_sum = current_sum

if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")
