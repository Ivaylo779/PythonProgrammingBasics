start = int(input())
end = int(input())

for a in range(start, end + 1):
    for b in range(start, end + 1):
        for c in range(start, end + 1):
            for d in range(start, end + 1):
                if (a % 2 != d % 2) and (a > d) and ((b + c) % 2 == 0):
                    print(f"{a}{b}{c}{d}", end= " ")
