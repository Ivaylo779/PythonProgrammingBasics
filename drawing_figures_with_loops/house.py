n = int(input())

roof_rows = (n + 1) // 2
stars = 1 if n % 2 == 1 else 2

for _ in range(roof_rows):
    side = (n - stars) // 2
    print('-' * side + '*' * stars + '-' * side)
    stars += 2

for _ in range(n // 2):
    print('|' + '*' * (n - 2) + '|')
