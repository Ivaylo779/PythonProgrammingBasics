n = int(input())

print("*" * (2 * n) + " " * n + "*" * (2 * n))

for row in range(n - 2):
    left_lens = "*" + "/" * (2 * n - 2) + "*"
    middle_row = (n - 1) // 2 - 1
    if row == middle_row:
        middle = "|" * n
    else:
        middle = " " * n

    right_lens = "*" + "/" * (2 * n - 2) + "*"

    print(left_lens + middle + right_lens)

print("*" * (2 * n) + " " * n + "*" * (2 * n))