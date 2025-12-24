start = int(input())
end = int(input())
magic_number = int(input())

combinations = 0
found = False

for num_1 in range(start, end + 1):
    for num_2 in range(start, end + 1):
        combinations += 1
        if num_1 + num_2 == magic_number:
            print(f"Combination N:{combinations} ({num_1} + {num_2} = {magic_number})")
            found = True
            break

    if found:
        break

else:
    print(f"{combinations} combinations - neither equals {magic_number}")
