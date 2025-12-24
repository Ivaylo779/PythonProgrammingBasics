stadium_capacity = int(input())
fan_number = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(1, fan_number + 1):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

print(f"{(sector_a / fan_number) * 100:.2f}%")
print(f"{(sector_b / fan_number) * 100:.2f}%")
print(f"{(sector_v / fan_number) * 100:.2f}%")
print(f"{(sector_g / fan_number) * 100:.2f}%")
print(f"{(fan_number / stadium_capacity) * 100:.2f}%")