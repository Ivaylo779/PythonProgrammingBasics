n = int(input())

for number in range(1111, 10000):
    number_str = str(number)
    is_special = True

    for digit_char in number_str:
        digit = int(digit_char)
        if digit == 0 or n % digit != 0:
            is_special = False
            break

    if is_special:
        print(number, end=" ")
