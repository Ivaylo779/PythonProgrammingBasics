from math import ceil

brioche_number = int(input())
sugar_packets = 0
flour_packets = 0
max_spent_sugar = 0
max_spent_flour = 0

for _ in range(1, brioche_number + 1):
    spent_sugar = int(input())
    spent_flour = int(input())
    sugar_packets += spent_sugar
    flour_packets += spent_flour
    if spent_sugar > max_spent_sugar:
        max_spent_sugar = spent_sugar
    if spent_flour > max_spent_flour:
        max_spent_flour = spent_flour

if sugar_packets >= 950:
    sugar_packet_number = sugar_packets / 950
if flour_packets >= 750:
    flour_packet_number = flour_packets / 750

print(f"Sugar: {ceil(sugar_packet_number)}")
print(f"Flour: {ceil(flour_packet_number)}")
print(f"Max used flour is {max_spent_flour} grams, max used sugar is {max_spent_sugar} grams.")