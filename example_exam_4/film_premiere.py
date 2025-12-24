projection = input()
movie_bundle = input()
tickets = int(input())

if projection == "John Wick":
    if movie_bundle == "Drink":
        price = 12
    elif movie_bundle == "Popcorn":
        price = 15
    elif movie_bundle == "Menu":
        price = 19
elif projection == "Star Wars":
    if movie_bundle == "Drink":
        price = 18
    elif movie_bundle == "Popcorn":
        price = 25
    elif movie_bundle == "Menu":
        price = 30
if projection == "Jumanji":
    if movie_bundle == "Drink":
        price = 9
    elif movie_bundle == "Popcorn":
        price = 11
    elif movie_bundle == "Menu":
        price = 14

total_price = price * tickets

if projection == "Star Wars" and tickets >= 4:
    total_price *= 0.70

elif projection == "Jumanji" and tickets == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
