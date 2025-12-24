from math import floor,ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

MAGNOLIA_PRICE = 3.25
HYACINTH_PRICE = 4.00
ROSE_PRICE = 3.50
CACTUS_PRICE = 8.00

total_sum = magnolias * MAGNOLIA_PRICE + hyacinths * HYACINTH_PRICE + roses * ROSE_PRICE + cacti * CACTUS_PRICE
taxes = total_sum * 0.05
winnings = total_sum - taxes

if winnings >= gift_price:
    diff = winnings - gift_price
    print(f"She is left with {(floor(diff))} leva.")
else:
    diff = gift_price - winnings
    print(f"She will have to borrow {(ceil(diff))} leva.")