BRIOCHE = 3.20
EGGS = 4.35
COOKIES = 5.40
EGG_PAINT = 0.15

brioche_number = int(input())
egg_number = int(input())
cookie_kgs = int(input())

brioche_price = BRIOCHE * brioche_number
eggs_price = EGGS * egg_number
cookies_price = COOKIES * cookie_kgs
egg_paint_price = egg_number * 12 * EGG_PAINT

total_price = brioche_price + cookies_price + eggs_price + egg_paint_price

print(f"{total_price:.2f}")