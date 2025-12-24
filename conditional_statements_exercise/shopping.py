budget = float(input())
graphics_cards = int(input())
pc_processors = int(input())
ram_memories = int(input())

SINGLE_CARD_PRICE = 250

graphics_card_price = graphics_cards * SINGLE_CARD_PRICE
processor_price  = graphics_card_price * 0.35
ram_price = graphics_card_price * 0.10

total_sum = graphics_card_price + pc_processors * processor_price + ram_memories * ram_price

if graphics_cards > pc_processors:
    total_sum -= total_sum * 0.15

if budget >= total_sum:
    leftover = budget - total_sum
    print(f"You have {leftover:.2f} leva left!")
else:
    not_enough = total_sum - budget
    print(f"Not enough money! You need {not_enough:.2f} leva more!")
