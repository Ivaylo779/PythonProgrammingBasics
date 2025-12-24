n = int(input())
k = (n - 1) // 2
for i in range(2 * k + 1):
    left_right = abs(k - i)
    mid = n - 2 * left_right - 2
    if mid >= 0:
        print('-' * left_right + '*' + '-' * mid + '*' + '-' * left_right)
    else:
        print('-' * left_right + '*' + '-' * left_right)