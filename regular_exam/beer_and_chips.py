from math import ceil

fan_name = input()
budget = float(input())
beer_bottle_number = int(input())
chips_packet_number = int(input())

total_beer_price = 1.20 * beer_bottle_number
chips_packet_price = total_beer_price * 0.45
total_chips_price = ceil(chips_packet_price * chips_packet_number)
total_sum = total_beer_price + total_chips_price

if total_sum <= budget:
    diff = budget - total_sum
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")
else:
    diff = total_sum - budget
    print(f"{fan_name} needs {diff:.2f} more leva!")