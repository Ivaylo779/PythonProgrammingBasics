detergent_bottles = int(input())
count = 0
plates = 0
pots = 0

detergent_quantity = detergent_bottles * 750

while True:
    dishes = input()
    if dishes == "End":
        break
    dishes = int(dishes)
    count += 1
    if count % 3 == 0:
        detergent_quantity -= dishes * 15
        pots += dishes
    else:
        detergent_quantity -= dishes * 5
        plates += dishes
    if detergent_quantity < 0:
        break


if detergent_quantity >= 0:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {detergent_quantity} ml.")
else:
    print(f"Not enough detergent, {abs(detergent_quantity)} ml. more necessary!")