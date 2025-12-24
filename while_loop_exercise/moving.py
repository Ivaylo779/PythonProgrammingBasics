width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
space_needed = 0
boxes = ""

while True:
    boxes = input()
    if boxes == "Done":
        break
    boxes_count = int(boxes)
    space_needed += boxes_count
    if space_needed >= free_space:
        break

if boxes == "Done":
    remaining_space = free_space - space_needed
    print(f"{remaining_space} Cubic meters left.")
if space_needed >= free_space:
    diff = space_needed - free_space
    print(f"No more free space! You need {diff} Cubic meters more.")