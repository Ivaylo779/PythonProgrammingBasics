painted_egg_number = int(input())
max_eggs = 0
red = 0
orange = 0
blue = 0
green = 0

for _ in range(painted_egg_number):
    egg_color = input()
    if egg_color == "red":
        red += 1
    elif egg_color == "orange":
        orange += 1
    elif egg_color == "blue":
        blue += 1
    elif egg_color == "green":
        green += 1

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")

if red > max_eggs:
    max_eggs = red
    egg_color = "red"
if orange > max_eggs:
    max_eggs = orange
    egg_color = "orange"
if blue > max_eggs:
    max_eggs = blue
    egg_color = "blue"
if green > max_eggs:
    max_eggs = green
    egg_color = "green"

print(f"Max eggs: {max_eggs} -> {egg_color}")


    