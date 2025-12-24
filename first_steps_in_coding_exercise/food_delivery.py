CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15

number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

chicken_price = number_of_chicken_menus * CHICKEN_MENU
fish_price = number_of_fish_menus * FISH_MENU
vegetarian_price = number_of_vegetarian_menus * VEGETARIAN_MENU

price_for_menus = chicken_price + fish_price + vegetarian_price
dessert_price = price_for_menus * 0.20
total_price = price_for_menus + dessert_price
final_price = total_price + 2.50

print(final_price)