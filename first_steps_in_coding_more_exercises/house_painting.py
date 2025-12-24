x = float(input())
y = float(input())
h = float(input())

front_back_area = 2 * (x * x) - 1.2 * 2
side_walls_area = 2 * (x * y - 1.5 * 1.5)

green_area = front_back_area + side_walls_area
green_paint = green_area / 3.4

rect_roof_area = 2 * (x * y)
tri_roof_area = 2 * (x * h / 2)

red_area = rect_roof_area + tri_roof_area
red_paint = red_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
