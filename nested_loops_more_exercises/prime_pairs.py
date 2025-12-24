first_pair_start = int(input())
second_pair_start = int(input())
first_pair_difference = int(input())
second_pair_difference = int(input())

pass_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for first_pair in range(first_pair_start, first_pair_start + first_pair_difference + 1):
    if first_pair not in pass_nums:
        continue
    for second_pair in range(second_pair_start, second_pair_start + second_pair_difference + 1):
        if second_pair not in pass_nums:
            continue

        full_number = str(first_pair) + str(second_pair)

        print(full_number)