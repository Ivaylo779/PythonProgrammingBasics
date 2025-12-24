BASKET = 1.50
WREATH = 3.80
CHOCOLATE_BUNNY = 7

total_sum = 0

clients = int(input())

for _ in range(1, clients + 1):
    items = 0
    client_sum = 0
    while True:
        purchase = input()
        if purchase == "Finish":
            if items % 2 == 0:
                client_sum -= client_sum * 0.20
            print(f"You purchased {items} items for {client_sum:.2f} leva.")
            break
        items += 1
        if purchase == "basket":
             client_sum += BASKET
        elif purchase == "wreath":
            client_sum += WREATH
        elif purchase == "chocolate bunny":
            client_sum += CHOCOLATE_BUNNY
    total_sum += client_sum

print(f"Average bill per client is: {(total_sum / clients):.2f} leva.")
