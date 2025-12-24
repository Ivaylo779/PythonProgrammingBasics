from math import ceil

people = int(input())
entry_fee = float(input())
deckchair_price = float(input())
umbrella_price = float(input())

total_entry_fee = people * entry_fee
umbrella_number = ceil(people / 2)
total_umbrella_price = umbrella_number * umbrella_price
deckchair_number = ceil(people * 0.75)
total_deckchair_price = deckchair_number * deckchair_price

total_price = total_entry_fee + total_umbrella_price + total_deckchair_price

print(f"{total_price:.2f} lv." )
