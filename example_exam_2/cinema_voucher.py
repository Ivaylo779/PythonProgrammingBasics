voucher_value = int(input())
tickets = 0
other = 0

while True:
    purchase = input()
    if purchase == "End":
        break

    if len(purchase) > 8:
        first_index = purchase[0]
        second_index = purchase[1]
        first_char_value = ord(first_index)
        second_char_value = ord(second_index)
        char_sum = first_char_value + second_char_value
        if char_sum > voucher_value:
            break
        tickets += 1
        voucher_value -= char_sum
    else:
        first_index = purchase[0]
        char_sum = ord(first_index)
        if char_sum > voucher_value:
            break
        other += 1
        voucher_value -= char_sum

print(f"{tickets}")
print(f"{other}")
