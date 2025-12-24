lenght_in_cm = int(input())
widt_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())

volume = (lenght_in_cm * widt_in_cm * height_in_cm) / 1000
space_for_water = volume - (volume * (percentage / 100))

print(space_for_water)
