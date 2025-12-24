from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_number = int(input())
sneaker_pairs = int(input())

sneakers_price = tennis_racket_price * 1/6

total_sum = tennis_racket_number * tennis_racket_price + sneaker_pairs * sneakers_price
other_equipment = total_sum * 0.20
final_sum = total_sum + other_equipment

djokovic_sum = final_sum * 1/8
sponsor_sum = final_sum * 7/8

print(f"Price to be paid by Djokovic {floor(djokovic_sum)}")
print(f"Price to be paid by sponsors {ceil(sponsor_sum)}")

