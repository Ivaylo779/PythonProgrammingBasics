figure = input()

if figure == "square":
    side_1 = float(input())
    area = side_1 * side_1
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    from math import pi
    area = pi * radius * radius
    print(f"{area:.3f}")
else:
    side_1 = float(input())
    height = float(input())
    area = (side_1 * height) / 2
    print(f"{area:.3f}")

