expected_sum = int(input())

cash_sum = 0
card_sum = 0
cash_count = 0
card_count = 0
turn = 1
total_collected = 0

while True:
    item = input()
    if item == "End":
        print("Failed to collect required money for charity.")
        break

    price = int(item)

    if turn == 1:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash_sum += price
            cash_count += 1
            total_collected += price
        turn = 2
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            card_sum += price
            card_count += 1
            total_collected += price
        turn = 1

    if total_collected >= expected_sum:
        print(f"Average CS: {cash_sum / cash_count:.2f}")
        print(f"Average CC: {card_sum / card_count:.2f}")
        break
