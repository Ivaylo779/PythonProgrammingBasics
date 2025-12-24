n = int(input())

for number in range(0, n + 1):
    if number % 2 == 0:
        number = 2 ** number
        print(number)


