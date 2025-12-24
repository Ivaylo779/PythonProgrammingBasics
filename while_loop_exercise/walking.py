steps = input()
walk_distance = 0

while True:
    if steps == "Going home":
        steps_made = int(input())
        walk_distance += steps_made
        if walk_distance >= 10000:
            print("Goal reached! Good job!")
            diff = walk_distance - 10000
            print(f"{diff} steps over the goal!")
            break
        else:
            diff = 10000 - walk_distance
            print(f"{diff} more steps to reach goal.")
            break
    new_input = int(steps)
    walk_distance += new_input
    if walk_distance >= 10000:
        print("Goal reached! Good job!")
        diff = walk_distance - 10000
        print(f"{diff} steps over the goal!")
        break
    steps = input()

