import sys

film_number = int(input())
all_ratings = 0

high_rating = -sys.maxsize
low_rating = sys.maxsize

for _ in range(1, film_number + 1):
    film_name = input()
    film_rating = float(input())
    all_ratings += film_rating
    if film_rating > high_rating:
        high_rating = film_rating
        name_1 = film_name
    elif film_rating < low_rating:
        low_rating = film_rating
        name_2 = film_name

average = all_ratings / film_number

print(f"{name_1} is with highest rating: {high_rating:.1f}")
print(f"{name_2} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {average:.1f}")