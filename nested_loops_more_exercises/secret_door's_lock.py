upper_limit_of_hundreds = int(input())
upper_limit_of_tens = int(input())
upper_limit_of_ones = int(input())

prime_numbers = [2,3,5,7]

for hundreds in range(1, upper_limit_of_hundreds + 1):
    if hundreds % 2 != 0:
        continue
    for tens in range(1, upper_limit_of_tens + 1):
        if tens not in prime_numbers:
            continue
        for ones in range(1, upper_limit_of_ones + 1):
            if ones % 2 != 0:
                continue
            print(hundreds, tens, ones)


