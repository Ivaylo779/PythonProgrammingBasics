from math import ceil

wall_height = int(input())
wall_width = int(input())
no_paint_area = int(input())

total_area = 4 * wall_height * wall_width
area_to_paint = total_area - (total_area * no_paint_area / 100)
area_to_paint = ceil(area_to_paint)

total_paint = 0

while True:
    command = input()

    if command == "Tired!":
        remaining = area_to_paint - total_paint
        print(f"{remaining} quadratic m left.")
        break

    paint = int(command)
    total_paint += paint

    if total_paint >= area_to_paint:
        leftover = total_paint - area_to_paint
        if leftover > 0:
            print(f"All walls are painted and you have {leftover} l paint left!")
        else:
            print("All walls are painted! Great job, Pesho!")
        break