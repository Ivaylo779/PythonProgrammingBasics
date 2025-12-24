desired_height = int(input())
count = 0
fail_count = 0
lath = desired_height - 30

while True:
    jump_height = int(input())
    count += 1
    if jump_height > lath:
        lath += 5
        fail_count = 0
        if lath > desired_height:
            print(f"Tihomir succeeded, he jumped over {lath - 5}cm "
                  f"after {count} jumps.")
            break
    else:
        fail_count += 1
        if fail_count == 3:
            print(f"Tihomir failed at {lath}cm after "
                  f"{count} jumps.")
            break
